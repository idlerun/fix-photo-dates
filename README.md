---
page: https://idle.run/fix-photo-dates
title: Automatic EXIF Date Fixer
tags: python
date: 2016-05-04
---

## [fix-photo-dates.py](https://github.com/idlerun/fix-photo-dates/blob/master/fix-photo-dates.py)

A simple OSX utility I wrote to fix dates on my photos and videos.

Requires a photo or video with a name like any of the following:

```text
20160501_083935.mp4
VID_20160501_083935.mp4
IMG_20160501_083935.jpg
```

* Standardizes the file name by removing the `VID_` or `IMG_` prefix if any
* Uses both `exiftool` and `SetFile` to set the photo/video creation date according to the date in the file name

This is most useful when operations like trimming a video cause the "created" date on a video to be reset to the current date and screws up sorting by date.
