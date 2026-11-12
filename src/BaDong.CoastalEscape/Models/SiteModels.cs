namespace BaDong.CoastalEscape.Models;

public sealed class Destination
{
    public string Id { get; set; } = string.Empty;
    public string Slug { get; set; } = string.Empty;
    public string Name { get; set; } = string.Empty;
    public string Subtitle { get; set; } = string.Empty;
    public string Category { get; set; } = string.Empty;
    public string ShortDescription { get; set; } = string.Empty;
    public List<string> Description { get; set; } = [];
    public string Thumbnail { get; set; } = string.Empty;
    public string HeroImage { get; set; } = string.Empty;
    public int ThumbnailWidth { get; set; }
    public int HeroWidth { get; set; }
    public string ImageAlt { get; set; } = string.Empty;
    public string ImageLocation { get; set; } = string.Empty;
    public string ImageAttribution { get; set; } = string.Empty;
    public string ImageLicense { get; set; } = string.Empty;
    public string ImageSourceUrl { get; set; } = string.Empty;
    public string ImageVerificationStatus { get; set; } = string.Empty;
    public List<string> Tags { get; set; } = [];
    public string MapUrl { get; set; } = string.Empty;
    public List<string> SourceUrls { get; set; } = [];
    public string UpdatedAt { get; set; } = string.Empty;
}

public sealed class Food
{
    public string Id { get; set; } = string.Empty;
    public string Slug { get; set; } = string.Empty;
    public string Name { get; set; } = string.Empty;
    public string Category { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string Image { get; set; } = string.Empty;
    public string Thumbnail { get; set; } = string.Empty;
    public int ThumbnailWidth { get; set; }
    public int ImageWidth { get; set; }
    public string Alt { get; set; } = string.Empty;
    public string ImageLocation { get; set; } = string.Empty;
    public string ImageAttribution { get; set; } = string.Empty;
    public string ImageLicense { get; set; } = string.Empty;
    public string ImageSourceUrl { get; set; } = string.Empty;
    public string ImageVerificationStatus { get; set; } = string.Empty;
    public string BestEnjoyed { get; set; } = string.Empty;
    public string Note { get; set; } = string.Empty;
    public List<string> SourceUrls { get; set; } = [];
}

public sealed class GalleryPhoto
{
    public string Id { get; set; } = string.Empty;
    public string Image { get; set; } = string.Empty;
    public string Thumbnail { get; set; } = string.Empty;
    public int ThumbnailWidth { get; set; }
    public int ThumbnailHeight { get; set; }
    public int ImageWidth { get; set; }
    public int ImageHeight { get; set; }
    public string Alt { get; set; } = string.Empty;
    public string Caption { get; set; } = string.Empty;
    public string Category { get; set; } = string.Empty;
    public string Author { get; set; } = string.Empty;
    public string License { get; set; } = string.Empty;
    public string SourceUrl { get; set; } = string.Empty;
    public string ActualLocation { get; set; } = string.Empty;
    public string VerificationStatus { get; set; } = string.Empty;
}

public sealed class Itinerary
{
    public string Id { get; set; } = string.Empty;
    public string Title { get; set; } = string.Empty;
    public string DurationLabel { get; set; } = string.Empty;
    public string Summary { get; set; } = string.Empty;
    public List<ItineraryStop> Stops { get; set; } = [];
}

public sealed class ItineraryStop
{
    public string TimeLabel { get; set; } = string.Empty;
    public string Title { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string Slug { get; set; } = string.Empty;
    public string Image { get; set; } = string.Empty;
    public string ImageAlt { get; set; } = string.Empty;
}

public sealed class FaqItem
{
    public string Id { get; set; } = string.Empty;
    public string Question { get; set; } = string.Empty;
    public string Answer { get; set; } = string.Empty;
    public List<string> SourceUrls { get; set; } = [];
}

public sealed class SiteInfo
{
    public string Name { get; set; } = "BA ĐỘNG — Coastal Escape";
    public string Tagline { get; set; } = "Nơi biển chạm vào nhịp sống miền Tây.";
    public string Region { get; set; } = "Trà Vinh coast · Mekong Delta";
    public string AdministrativeLocation { get; set; } = string.Empty;
    public string AcademicDisclaimer { get; set; } = string.Empty;
    public string UpdatedAt { get; set; } = string.Empty;
    public string MapUrl { get; set; } = string.Empty;
    public List<SourceLink> SourceLinks { get; set; } = [];
}

public sealed class SourceLink
{
    public string Label { get; set; } = string.Empty;
    public string Url { get; set; } = string.Empty;
}
