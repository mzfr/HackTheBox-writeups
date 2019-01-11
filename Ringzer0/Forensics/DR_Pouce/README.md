# Dr Pouce

__PROBLEM__

Find in which city DR Pouce is keeped ! Then find who is the evil man?

answer format : cityfirstnamelastname

__SOLUTION__

So we are given two things, image and pdf and we are supposed to find the name of the evil man, along with the city DR. Pouce is kept.

If you'll look the `exif` data of the PDF you'll get:
```
➜ exiftool DR_Pouce.pdf
ExifTool Version Number         : 11.11
File Name                       : DR_Pouce.pdf
Directory                       : .
File Size                       : 16 kB
File Modification Date/Time     : 2014:03:19 21:30:22+05:30
File Access Date/Time           : 0000:00:00 00:00:00
File Inode Change Date/Time     : 2018:12:08 21:40:11+05:30
File Permissions                : rw-rw-r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.4
Linearized                      : No
Page Count                      : 1
Language                        : fr-CA
Author                          : Steve Finger
Creator                         : Writer
Producer                        : LibreOffice 3.5
Create Date                     : 2014:03:19 21:30:22-04:00
```

Meaning evil man is `Steve Finger`

And looking at the exif data of the image
```
➜ exiftool DR_Pouce.jpg
ExifTool Version Number         : 11.11
File Name                       : DR_Pouce.jpg
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2014:03:19 21:17:20+05:30
File Access Date/Time           : 0000:00:00 00:00:00
File Inode Change Date/Time     : 2018:12:08 21:40:12+05:30
File Permissions                : rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Big-endian (Motorola, MM)
Make                            : LGE
Camera Model Name               : Nexus 5
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exposure Time                   : 1/30
F Number                        : 2.4
ISO                             : 1034
Exif Version                    : 0220
Date/Time Original              : 2014:03:19 20:33:17
Create Date                     : 2014:03:19 20:33:17
Components Configuration        : Y, Cb, Cr, -
Shutter Speed Value             : 1/30
Aperture Value                  : 2.4
Exposure Compensation           : 0
Flash                           : No Flash
Focal Length                    : 4.0 mm
Flashpix Version                : 0100
Color Space                     : sRGB
Exif Image Width                : 2448
Exif Image Height               : 3264
Interoperability Index          : R98 - DCF basic file (sRGB)
Interoperability Version        : 0100
GPS Latitude Ref                : North
GPS Longitude Ref               : West
GPS Img Direction Ref           : Magnetic North
GPS Img Direction               : 237
Compression                     : JPEG (old-style)
Thumbnail Offset                : 720
Thumbnail Length                : 5310
Image Width                     : 2448
Image Height                    : 3264
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Aperture                        : 2.4
GPS Latitude                    : 44 deg 38' 46.43" N
GPS Longitude                   : 63 deg 34' 23.83" W
GPS Position                    : 44 deg 38' 46.43" N, 63 deg 34' 23.83" W
Image Size                      : 2448x3264
Megapixels                      : 8.0
Shutter Speed                   : 1/30
Thumbnail Image                 : (Binary data 5310 bytes, use -b option to extract)
Focal Length                    : 4.0 mm
Light Value                     : 4.1

```

There you'll notice the Latitude and longitudes. Simply convert them and you'll get the city as `halifax`.

FLAG - `halifaxstevefinger`
