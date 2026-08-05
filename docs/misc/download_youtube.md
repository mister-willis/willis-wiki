# Download Videos from YouTube

1. Download a current version of [yt-dlp](https://github.com/yt-dlp/yt-dlp#installation).

2. Run this terminal command, replacing `TITLE` and `YOUTUBE_URL`.

    ```bash
    yt-dlp \
      -f "bv*[ext=mp4][vcodec^=avc1]+ba[ext=m4a]/b[ext=mp4]/best" \
      --write-subs \
      --write-auto-subs \
      --sub-langs "en.*,-live_chat" \
      --sub-format vtt \
      --merge-output-format mp4 \
      -o "TITLE.%(ext)s" \
      "YOUTUBE_URL"
    ```
