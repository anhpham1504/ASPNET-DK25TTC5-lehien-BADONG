using System.Collections.Concurrent;
using System.Text.Json;
using System.Net.Http.Json;
using BaDong.CoastalEscape.Models;

namespace BaDong.CoastalEscape.Services;

public sealed class ContentService(HttpClient httpClient)
{
    private readonly JsonSerializerOptions _jsonOptions = new(JsonSerializerDefaults.Web);
    private readonly ConcurrentDictionary<string, object> _cache = [];

    public Task<IReadOnlyList<Destination>> GetDestinationsAsync() => LoadAsync<Destination>("data/destinations.json");
    public Task<IReadOnlyList<Food>> GetFoodsAsync() => LoadAsync<Food>("data/foods.json");
    public Task<IReadOnlyList<GalleryPhoto>> GetGalleryAsync() => LoadAsync<GalleryPhoto>("data/gallery.json");
    public Task<IReadOnlyList<Itinerary>> GetItinerariesAsync() => LoadAsync<Itinerary>("data/itineraries.json");
    public Task<IReadOnlyList<FaqItem>> GetFaqAsync() => LoadAsync<FaqItem>("data/faq.json");
    public Task<SiteInfo> GetSiteInfoAsync() => LoadObjectAsync("data/site-info.json");

    private async Task<IReadOnlyList<T>> LoadAsync<T>(string path)
    {
        if (_cache.TryGetValue(path, out var cached) && cached is IReadOnlyList<T> items)
        {
            return items;
        }

        try
        {
            var result = await httpClient.GetFromJsonAsync<List<T>>(path, _jsonOptions) ?? [];
            _cache[path] = result;
            return result;
        }
        catch (HttpRequestException)
        {
            return [];
        }
        catch (JsonException)
        {
            return [];
        }
        catch (NotSupportedException)
        {
            return [];
        }
        catch (TaskCanceledException)
        {
            return [];
        }
    }

    private async Task<SiteInfo> LoadObjectAsync(string path)
    {
        if (_cache.TryGetValue(path, out var cached) && cached is SiteInfo info)
        {
            return info;
        }

        try
        {
            var result = await httpClient.GetFromJsonAsync<SiteInfo>(path, _jsonOptions) ?? new SiteInfo();
            _cache[path] = result;
            return result;
        }
        catch (HttpRequestException)
        {
            return new SiteInfo();
        }
        catch (JsonException)
        {
            return new SiteInfo();
        }
        catch (NotSupportedException)
        {
            return new SiteInfo();
        }
        catch (TaskCanceledException)
        {
            return new SiteInfo();
        }
    }
}
