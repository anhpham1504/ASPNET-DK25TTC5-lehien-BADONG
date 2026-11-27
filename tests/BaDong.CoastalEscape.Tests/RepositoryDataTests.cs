using System.Text.Json;
using BaDong.CoastalEscape.Models;

namespace BaDong.CoastalEscape.Tests;

public sealed class RepositoryDataTests
{
    private static readonly JsonSerializerOptions JsonOptions = new(JsonSerializerDefaults.Web);
    private static string TestDataRoot => Path.Combine(AppContext.BaseDirectory, "TestData");
    private static string DataRoot => Path.Combine(TestDataRoot, "data");

    [Fact]
    public void EveryJsonDocument_IsSyntacticallyValid()
    {
        var files = Directory.GetFiles(DataRoot, "*.json");
        Assert.NotEmpty(files);

        foreach (var file in files)
        {
            using var document = JsonDocument.Parse(File.ReadAllText(file));
            Assert.NotEqual(JsonValueKind.Undefined, document.RootElement.ValueKind);
        }
    }

    [Fact]
    public void ContentJson_DeserializesIntoProductionModels()
    {
        Assert.NotEmpty(ReadList<Destination>("destinations.json"));
        Assert.NotEmpty(ReadList<Food>("foods.json"));
        Assert.NotEmpty(ReadList<GalleryPhoto>("gallery.json"));
        Assert.NotEmpty(ReadList<Itinerary>("itineraries.json"));
        Assert.NotEmpty(ReadList<FaqItem>("faq.json"));

        var siteInfo = Read<SiteInfo>("site-info.json");
        Assert.False(string.IsNullOrWhiteSpace(siteInfo.Name));
    }

    [Fact]
    public void ContentIds_AreUniqueWithinEachCollection()
    {
        AssertUnique(ReadList<Destination>("destinations.json").Select(item => item.Id), "destination ID");
        AssertUnique(ReadList<Food>("foods.json").Select(item => item.Id), "food ID");
        AssertUnique(ReadList<GalleryPhoto>("gallery.json").Select(item => item.Id), "gallery ID");
        AssertUnique(ReadList<Itinerary>("itineraries.json").Select(item => item.Id), "itinerary ID");
        AssertUnique(ReadList<FaqItem>("faq.json").Select(item => item.Id), "FAQ ID");
    }

    [Fact]
    public void RouteSlugs_AreUniqueWithinEachCollection()
    {
        AssertUnique(ReadList<Destination>("destinations.json").Select(item => item.Slug), "destination slug");
        AssertUnique(ReadList<Food>("foods.json").Select(item => item.Slug), "food slug");
    }

    [Fact]
    public void ReferencedLocalImages_Exist()
    {
        var paths = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

        foreach (var item in ReadList<Destination>("destinations.json"))
        {
            paths.Add(item.Thumbnail);
            paths.Add(item.HeroImage);
        }

        foreach (var item in ReadList<Food>("foods.json"))
        {
            paths.Add(item.Thumbnail);
            paths.Add(item.Image);
        }

        foreach (var item in ReadList<GalleryPhoto>("gallery.json"))
        {
            paths.Add(item.Thumbnail);
            paths.Add(item.Image);
        }

        foreach (var stop in ReadList<Itinerary>("itineraries.json").SelectMany(item => item.Stops))
        {
            paths.Add(stop.Image);
        }

        foreach (var item in ReadList<ImageManifestEntry>("image-manifest.json"))
        {
            paths.Add(item.Filename);
            foreach (var variant in item.ResponsiveVariants)
            {
                paths.Add(variant);
            }
        }

        var missing = paths
            .Where(path => !File.Exists(ResolveAsset(path)))
            .OrderBy(path => path, StringComparer.OrdinalIgnoreCase)
            .ToList();

        Assert.True(missing.Count == 0, $"Missing local images: {string.Join(", ", missing)}");
    }

    [Fact]
    public void ContentRequiredByTheUi_IsPresent()
    {
        foreach (var item in ReadList<Destination>("destinations.json"))
        {
            AssertNotBlank(item.Id, "destination ID");
            AssertNotBlank(item.Slug, $"destination {item.Id} slug");
            AssertNotBlank(item.Name, $"destination {item.Id} name");
            AssertNotBlank(item.Category, $"destination {item.Id} category");
            AssertNotBlank(item.ShortDescription, $"destination {item.Id} short description");
            Assert.NotEmpty(item.Description);
            AssertNotBlank(item.Thumbnail, $"destination {item.Id} thumbnail");
            AssertNotBlank(item.HeroImage, $"destination {item.Id} hero image");
            AssertNotBlank(item.ImageAlt, $"destination {item.Id} image alt");
            AssertNotBlank(item.ImageVerificationStatus, $"destination {item.Id} verification status");
            AssertNotBlank(item.MapUrl, $"destination {item.Id} map URL");
        }

        foreach (var item in ReadList<Food>("foods.json"))
        {
            AssertNotBlank(item.Id, "food ID");
            AssertNotBlank(item.Slug, $"food {item.Id} slug");
            AssertNotBlank(item.Name, $"food {item.Id} name");
            AssertNotBlank(item.Category, $"food {item.Id} category");
            AssertNotBlank(item.Description, $"food {item.Id} description");
            AssertNotBlank(item.Image, $"food {item.Id} image");
            AssertNotBlank(item.Thumbnail, $"food {item.Id} thumbnail");
            AssertNotBlank(item.Alt, $"food {item.Id} alt text");
            AssertNotBlank(item.ImageVerificationStatus, $"food {item.Id} verification status");
        }

        foreach (var item in ReadList<GalleryPhoto>("gallery.json"))
        {
            AssertNotBlank(item.Id, "gallery ID");
            AssertNotBlank(item.Image, $"gallery {item.Id} image");
            AssertNotBlank(item.Thumbnail, $"gallery {item.Id} thumbnail");
            AssertNotBlank(item.Alt, $"gallery {item.Id} alt text");
            AssertNotBlank(item.Caption, $"gallery {item.Id} caption");
            AssertNotBlank(item.VerificationStatus, $"gallery {item.Id} verification status");
        }

        foreach (var item in ReadList<Itinerary>("itineraries.json"))
        {
            AssertNotBlank(item.Id, "itinerary ID");
            AssertNotBlank(item.Title, $"itinerary {item.Id} title");
            AssertNotBlank(item.DurationLabel, $"itinerary {item.Id} duration");
            AssertNotBlank(item.Summary, $"itinerary {item.Id} summary");
            Assert.NotEmpty(item.Stops);

            foreach (var stop in item.Stops)
            {
                AssertNotBlank(stop.TimeLabel, $"itinerary {item.Id} stop time");
                AssertNotBlank(stop.Title, $"itinerary {item.Id} stop title");
                AssertNotBlank(stop.Description, $"itinerary {item.Id} stop description");
                AssertNotBlank(stop.Image, $"itinerary {item.Id} stop image");
                AssertNotBlank(stop.ImageAlt, $"itinerary {item.Id} stop image alt");
            }
        }

        foreach (var item in ReadList<FaqItem>("faq.json"))
        {
            AssertNotBlank(item.Id, "FAQ ID");
            AssertNotBlank(item.Question, $"FAQ {item.Id} question");
            AssertNotBlank(item.Answer, $"FAQ {item.Id} answer");
            Assert.NotEmpty(item.SourceUrls);
        }

        var siteInfo = Read<SiteInfo>("site-info.json");
        AssertNotBlank(siteInfo.Name, "site name");
        AssertNotBlank(siteInfo.Tagline, "site tagline");
        AssertNotBlank(siteInfo.Region, "site region");
        AssertNotBlank(siteInfo.AdministrativeLocation, "site administrative location");
        AssertNotBlank(siteInfo.AcademicDisclaimer, "site academic disclaimer");
        AssertNotBlank(siteInfo.UpdatedAt, "site update date");
        AssertNotBlank(siteInfo.MapUrl, "site map URL");
        Assert.NotEmpty(siteInfo.SourceLinks);

        foreach (var source in siteInfo.SourceLinks)
        {
            AssertNotBlank(source.Label, "site source label");
            AssertAbsoluteUrl(source.Url, "site source URL");
        }
    }

    [Fact]
    public void ItineraryDestinationReferences_ResolveToDestinationSlugs()
    {
        var destinationSlugs = ReadList<Destination>("destinations.json")
            .Select(item => item.Slug)
            .ToHashSet(StringComparer.OrdinalIgnoreCase);

        var unresolved = ReadList<Itinerary>("itineraries.json")
            .SelectMany(item => item.Stops)
            .Where(stop => !string.IsNullOrWhiteSpace(stop.Slug) && !destinationSlugs.Contains(stop.Slug))
            .Select(stop => stop.Slug)
            .Distinct(StringComparer.OrdinalIgnoreCase)
            .ToList();

        Assert.True(unresolved.Count == 0, $"Unresolved itinerary slugs: {string.Join(", ", unresolved)}");
    }

    [Fact]
    public void VerifiedImages_HaveCompleteProvenance()
    {
        var verified = ReadList<ImageManifestEntry>("image-manifest.json")
            .Where(item => item.VerificationStatus.StartsWith("VERIFIED", StringComparison.OrdinalIgnoreCase))
            .ToList();

        Assert.NotEmpty(verified);

        foreach (var item in verified)
        {
            AssertNotBlank(item.Filename, "verified image filename");
            AssertNotBlank(item.Title, $"image {item.Filename} title");
            AssertNotBlank(item.ActualLocation, $"image {item.Filename} actual location");
            AssertNotBlank(item.Photographer, $"image {item.Filename} photographer");
            AssertAbsoluteUrl(item.SourceUrl, $"image {item.Filename} source URL");
            AssertNotBlank(item.License, $"image {item.Filename} license");
            AssertNotBlank(item.Attribution, $"image {item.Filename} attribution");
        }
    }

    [Fact]
    public void RenderedVerifiedContent_HasCompleteImageMetadata()
    {
        foreach (var item in ReadList<Destination>("destinations.json")
                     .Where(item => item.ImageVerificationStatus.StartsWith("VERIFIED", StringComparison.OrdinalIgnoreCase)))
        {
            AssertNotBlank(item.ImageLocation, $"destination {item.Id} image location");
            AssertNotBlank(item.ImageAttribution, $"destination {item.Id} image attribution");
            AssertNotBlank(item.ImageLicense, $"destination {item.Id} image license");
            AssertAbsoluteUrl(item.ImageSourceUrl, $"destination {item.Id} image source URL");
        }

        foreach (var item in ReadList<Food>("foods.json")
                     .Where(item => item.ImageVerificationStatus.StartsWith("VERIFIED", StringComparison.OrdinalIgnoreCase)))
        {
            AssertNotBlank(item.ImageLocation, $"food {item.Id} image location");
            AssertNotBlank(item.ImageAttribution, $"food {item.Id} image attribution");
            AssertNotBlank(item.ImageLicense, $"food {item.Id} image license");
            AssertAbsoluteUrl(item.ImageSourceUrl, $"food {item.Id} image source URL");
        }

        foreach (var item in ReadList<GalleryPhoto>("gallery.json")
                     .Where(item => item.VerificationStatus.StartsWith("VERIFIED", StringComparison.OrdinalIgnoreCase)))
        {
            AssertNotBlank(item.ActualLocation, $"gallery {item.Id} actual location");
            AssertNotBlank(item.Author, $"gallery {item.Id} author");
            AssertNotBlank(item.License, $"gallery {item.Id} license");
            AssertAbsoluteUrl(item.SourceUrl, $"gallery {item.Id} source URL");
        }
    }

    [Fact]
    public void ImageManifest_CoversEveryPublishedImageWithExactCasing()
    {
        var registered = ReadList<ImageManifestEntry>("image-manifest.json")
            .SelectMany(item => item.ResponsiveVariants.Prepend(item.Filename))
            .ToHashSet(StringComparer.Ordinal);

        var published = Directory
            .GetFiles(Path.Combine(TestDataRoot, "images"), "*", SearchOption.AllDirectories)
            .Select(path => Path.GetRelativePath(TestDataRoot, path).Replace(Path.DirectorySeparatorChar, '/'))
            .ToHashSet(StringComparer.Ordinal);

        var unregistered = published.Except(registered, StringComparer.Ordinal).OrderBy(path => path).ToList();
        var missing = registered.Except(published, StringComparer.Ordinal).OrderBy(path => path).ToList();

        Assert.True(unregistered.Count == 0, $"Unregistered published images: {string.Join(", ", unregistered)}");
        Assert.True(missing.Count == 0, $"Manifest images missing from published assets: {string.Join(", ", missing)}");
    }

    [Fact]
    public void PendingDestinations_UseTheExplicitPlaceholderPolicy()
    {
        const string placeholder = "images/placeholders/pending-verification.svg";
        var pending = ReadList<Destination>("destinations.json")
            .Where(item => string.Equals(item.ImageVerificationStatus, "PENDING", StringComparison.OrdinalIgnoreCase))
            .ToList();

        foreach (var item in pending)
        {
            Assert.Equal(placeholder, item.Thumbnail);
            Assert.Equal(placeholder, item.HeroImage);
            Assert.True(string.IsNullOrWhiteSpace(item.ImageSourceUrl), $"Pending destination {item.Id} must not claim an image source.");
            Assert.Equal("PENDING", item.ImageLicense);
            Assert.Equal("PENDING", item.ImageLocation);
        }
    }

    private static T Read<T>(string filename) where T : class
    {
        var value = JsonSerializer.Deserialize<T>(File.ReadAllText(Path.Combine(DataRoot, filename)), JsonOptions);
        return Assert.IsType<T>(value);
    }

    private static IReadOnlyList<T> ReadList<T>(string filename)
    {
        var value = JsonSerializer.Deserialize<List<T>>(File.ReadAllText(Path.Combine(DataRoot, filename)), JsonOptions);
        return Assert.IsType<List<T>>(value);
    }

    private static string ResolveAsset(string relativePath)
    {
        var normalized = relativePath.Replace('/', Path.DirectorySeparatorChar);
        return Path.Combine(TestDataRoot, normalized);
    }

    private static void AssertUnique(IEnumerable<string> values, string label)
    {
        var duplicates = values
            .GroupBy(value => value, StringComparer.OrdinalIgnoreCase)
            .Where(group => group.Count() > 1)
            .Select(group => group.Key)
            .OrderBy(value => value, StringComparer.OrdinalIgnoreCase)
            .ToList();

        Assert.True(duplicates.Count == 0, $"Duplicate {label} values: {string.Join(", ", duplicates)}");
    }

    private static void AssertNotBlank(string value, string label) =>
        Assert.False(string.IsNullOrWhiteSpace(value), $"Missing {label}.");

    private static void AssertAbsoluteUrl(string value, string label)
    {
        AssertNotBlank(value, label);
        Assert.True(Uri.TryCreate(value, UriKind.Absolute, out _), $"Invalid {label}: {value}");
    }

    private sealed class ImageManifestEntry
    {
        public string Filename { get; set; } = string.Empty;
        public List<string> ResponsiveVariants { get; set; } = [];
        public string Title { get; set; } = string.Empty;
        public string ActualLocation { get; set; } = string.Empty;
        public string Photographer { get; set; } = string.Empty;
        public string SourceUrl { get; set; } = string.Empty;
        public string License { get; set; } = string.Empty;
        public string Attribution { get; set; } = string.Empty;
        public string VerificationStatus { get; set; } = string.Empty;
    }
}
