using System.Net;
using System.Text;
using BaDong.CoastalEscape.Services;

namespace BaDong.CoastalEscape.Tests;

public sealed class ContentServiceTests
{
    [Fact]
    public async Task GetDestinationsAsync_ReturnsValidJsonAndCachesTheResult()
    {
        const string json = """
            [
              {
                "id": "verified-destination",
                "slug": "verified-destination",
                "name": "Verified destination"
              }
            ]
            """;
        using var handler = new StubHttpMessageHandler(_ => JsonResponse(HttpStatusCode.OK, json));
        using var httpClient = CreateClient(handler);
        var service = new ContentService(httpClient);

        var first = await service.GetDestinationsAsync();
        var second = await service.GetDestinationsAsync();

        var destination = Assert.Single(first);
        Assert.Equal("verified-destination", destination.Id);
        Assert.Same(first, second);
        Assert.Equal(1, handler.RequestCount);
    }

    [Fact]
    public async Task GetDestinationsAsync_ReturnsEmptyForInvalidJson()
    {
        using var handler = new StubHttpMessageHandler(_ => JsonResponse(HttpStatusCode.OK, "{ invalid json"));
        using var httpClient = CreateClient(handler);
        var service = new ContentService(httpClient);

        var result = await service.GetDestinationsAsync();

        Assert.Empty(result);
    }

    [Fact]
    public async Task GetDestinationsAsync_ReturnsEmptyForHttpFailure()
    {
        using var handler = new StubHttpMessageHandler(_ => new HttpResponseMessage(HttpStatusCode.ServiceUnavailable));
        using var httpClient = CreateClient(handler);
        var service = new ContentService(httpClient);

        var result = await service.GetDestinationsAsync();

        Assert.Empty(result);
    }

    private static HttpClient CreateClient(HttpMessageHandler handler) => new(handler)
    {
        BaseAddress = new Uri("https://example.test/")
    };

    private static HttpResponseMessage JsonResponse(HttpStatusCode statusCode, string json) => new(statusCode)
    {
        Content = new StringContent(json, Encoding.UTF8, "application/json")
    };

    private sealed class StubHttpMessageHandler(Func<HttpRequestMessage, HttpResponseMessage> responseFactory) : HttpMessageHandler
    {
        public int RequestCount { get; private set; }

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            RequestCount++;
            return Task.FromResult(responseFactory(request));
        }
    }
}
