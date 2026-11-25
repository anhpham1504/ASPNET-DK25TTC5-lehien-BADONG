[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$pptx = Join-Path $root 'abs/BA-DONG-Coastal-Escape.pptx'
$pdf = Join-Path $root 'abs/BA-DONG-Coastal-Escape-Slides.pdf'
$powerPoint = New-Object -ComObject PowerPoint.Application
$presentation = $null
try {
    $presentation = $powerPoint.Presentations.Open($pptx, -1, 0, 0)
    $presentation.SaveAs($pdf, 32)
    Write-Output "Slides=$($presentation.Slides.Count)"
}
finally {
    if ($null -ne $presentation) { $presentation.Close() }
}
