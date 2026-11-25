[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$docx = Join-Path $root 'doc/BA-DONG-Coastal-Escape.docx'
$pdf = Join-Path $root 'pdf/BA-DONG-Coastal-Escape.pdf'
if (-not (Test-Path -LiteralPath $docx -PathType Leaf)) {
    throw 'Build the DOCX before exporting the review PDF.'
}

$word = New-Object -ComObject Word.Application
$document = $null
try {
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.AutomationSecurity = 3
    $document = $word.Documents.Open($docx, $false, $false)
    for ($pass = 0; $pass -lt 3; $pass++) {
        $null = $document.Fields.Update()
        $document.Repaginate()
        foreach ($toc in $document.TablesOfContents) { $toc.Update() }
        foreach ($figureList in $document.TablesOfFigures) { $figureList.Update() }
        $document.Repaginate()
    }
    $document.Save()
    $document.ExportAsFixedFormat($pdf, 17, $false, 0, 0, 1, 1, 0, $true, $false, 1, $true, $true, $false)
    "Pages=$($document.ComputeStatistics(2)); TOC=$($document.TablesOfContents.Count); CaptionLists=$($document.TablesOfFigures.Count)"
}
finally {
    if ($null -ne $document) { $document.Close($false) }
    $word.Quit()
}
