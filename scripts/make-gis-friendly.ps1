
$CountryToProcess = "Turkey
"

$DatasetLinksUrl = "https://minedbuildings.blob.core.windows.net/global-buildings/2023-03-13/global-buildings.geojsonl/RegionName%3DTurkey/quadkey%3D120323223/part-00092-459b9c51-35d7-4ec5-87f4-f9fc46a069a8.c000.csv.gz
"
$CompressedData = "compressed"
$ExpandedData = "expanded"

mkdir $CompressedData -Force
mkdir $ExpandedData  -Force

Function Expand-GZip{
    Param(
        $infile,
        $outfile
        )
    $inputData = New-Object System.IO.FileStream $inFile, ([IO.FileMode]::Open), ([IO.FileAccess]::Read), ([IO.FileShare]::Read)
    $output = New-Object System.IO.FileStream $outFile, ([IO.FileMode]::Create), ([IO.FileAccess]::Write), ([IO.FileShare]::None)
    $gzipStream = New-Object System.IO.Compression.GzipStream $inputData, ([IO.Compression.CompressionMode]::Decompress)
    $buffer = New-Object byte[](1024)
    while($true){
        $read = $gzipstream.Read($buffer, 0, 1024)
        if ($read -le 0){break}
        $output.Write($buffer, 0, $read)
        }
    $gzipStream.Close()
    $output.Close()
    $inputData.Close()
}

$resp = Invoke-WebRequest -Uri $DatasetLinksUrl
$links = ($resp.ToString() | ConvertFrom-Csv)

foreach ($link in $links) {
    if ($link.Location -eq $CountryToProcess) {
        Write-Host "Country: $($link.Location) QuadKey: $($link.QuadKey) Url: $($link.Url)"
        $downloadedGzip = "$CompressedData\$($link.Location)-$($link.QuadKey).csv.gz"
        $decompressedData = "$ExpandedData\$($link.Location)-$($link.QuadKey).geojsonl"
        Invoke-WebRequest -Uri $link.Url -OutFile $downloadedGzip
        Expand-GZip $downloadedGzip $decompressedData
    } 
}
