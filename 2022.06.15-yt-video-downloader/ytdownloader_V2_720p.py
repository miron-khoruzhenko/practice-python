from __future__ import unicode_literals
from tokenize import endpats
import yt_dlp
from yt_dlp.postprocessor.common import PostProcessor
import sys

# def progress_hook(d):
#     # if d['status'] == 'finished':
#     # if d['']


def post_hook(d):
    print('\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n\n\n\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n')

ydl_opts = {
    'format': 'bestvideo[ext=mp4][height<=720]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'noplaylist':False,
    'ignoreerrors' : True,
    'outtmpl': '[%(uploader)s] %(title)s.%(ext)s',
    "post_hooks" : [post_hook],
    
    # 'format': 'bestaudio/best',
    # 'extract_flat': True,
    # 'dump_single_json': True,
    # 'writethumbnail': False,
    # 'skip_unavailable_fragments': True, 
    # 'playliststart' : 224,
    # 'postprocessors': [{
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'mp3',
    #     'preferredquality': '128',
    # }],
    # 'progress_hooks' : [my_hook],
    # "throttledratelimit" : '100K',
    # "writethumbnail" : True,
}

# fileWithURLs = input("Name(path) of file with URLs> ")
fileWithURLs = sys.argv[1]
fileWithURLs = open(fileWithURLs)
try:
    linksArray = fileWithURLs.read().split("\n")
except:
    print(1)

try:
    print('\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n')
    for link in linksArray:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            endPath = ydl.download([link])
        
except:
    print(2)

print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n\t\t[Finished]\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n")




#TODO:пробелы между скачиваниями

#TODO:время скачивания

#TODO:настоящее время (время начала\конца скачивания)

#TODO:Если имя исполнителя и канала одинаковое то пусть будет только имя канала

#!Ошибки: Создать обработчик: Приватный плейлист \ нет видео \ не правильный URL \ в плейлисте нет видео.

#!Ошибки: Нет такого файла

#TODO:Вывод ошибки в консоль

#?Есть ли возможность создать отдельный плейлист и удалять оттуда скачанные видео

#TODO:txt файл со всеми названиями скачанных песен
# создать цикл для сканирования папки старых песен 

#TODO:Есть ли скачанные в плейлисте

#TODO: throttled rate RATE - посмотреть опцию для котроля скорости скачивания



# input("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n\t\t[Finished]\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n")

'''YoutubeDL class.
    YoutubeDL objects are the ones responsible of downloading the
    actual video file and writing it to disk if the user has requested
    it, among some other tasks. In most cases there should be one per
    program. As, given a video URL, the downloader doesn't know how to
    extract all the needed information, task that InfoExtractors do, it
    has to pass the URL to one of them.
    For this, YoutubeDL objects have a method that allows
    InfoExtractors to be registered in a given order. When it is passed
    a URL, the YoutubeDL object handles it to the first InfoExtractor it
    finds that reports being able to handle it. The InfoExtractor extracts
    all the information about the video or videos the URL refers to, and
    YoutubeDL process the extracted information, possibly using a File
    Downloader to download the video.
    YoutubeDL objects accept a lot of parameters. In order not to saturate
    the object constructor with arguments, it receives a dictionary of
    options instead. These options are available through the params
    attribute for the InfoExtractors to use. The YoutubeDL also
    registers itself as the downloader in charge for the InfoExtractors
    that are added to it, so this is a "mutual registration".
    
    Available options:
    username:          Username for authentication purposes.
    password:          Password for authentication purposes.
    videopassword:     Password for accessing a video.
    ap_mso:            Adobe Pass multiple-system operator identifier.
    ap_username:       Multiple-system operator account username.
    ap_password:       Multiple-system operator account password.
    usenetrc:          Use netrc for authentication instead.
    verbose:           Print additional info to stdout.
    quiet:             Do not print messages to stdout.
    no_warnings:       Do not print out anything for warnings.
    forceprint:        A list of templates to force print
    forceurl:          Force printing final URL. (Deprecated)
    forcetitle:        Force printing title. (Deprecated)
    forceid:           Force printing ID. (Deprecated)
    forcethumbnail:    Force printing thumbnail URL. (Deprecated)
    forcedescription:  Force printing description. (Deprecated)
    forcefilename:     Force printing final filename. (Deprecated)
    forceduration:     Force printing duration. (Deprecated)
    forcejson:         Force printing info_dict as JSON.
    dump_single_json:  Force printing the info_dict of the whole playlist
                       (or video) as a single JSON line.
    force_write_download_archive: Force writing download archive regardless
                       of 'skip_download' or 'simulate'.
    simulate:          Do not download the video files. If unset (or None),
                       simulate only if listsubtitles, listformats or list_thumbnails is used
    format:            Video format code. see "FORMAT SELECTION" for more details.
    allow_unplayable_formats:   Allow unplayable formats to be extracted and downloaded.
    ignore_no_formats_error: Ignore "No video formats" error. Usefull for
                       extracting metadata even if the video is not actually
                       available for download (experimental)
    format_sort:       How to sort the video formats. see "Sorting Formats"
                       for more details.
    format_sort_force: Force the given format_sort. see "Sorting Formats"
                       for more details.
    allow_multiple_video_streams:   Allow multiple video streams to be merged
                       into a single file
    allow_multiple_audio_streams:   Allow multiple audio streams to be merged
                       into a single file
    check_formats      Whether to test if the formats are downloadable.
                       Can be True (check all), False (check none)
                       or None (check only if requested by extractor)
    paths:             Dictionary of output paths. The allowed keys are 'home'
                       'temp' and the keys of OUTTMPL_TYPES (in utils.py)
    outtmpl:           Dictionary of templates for output names. Allowed keys
                       are 'default' and the keys of OUTTMPL_TYPES (in utils.py).
                       For compatibility with youtube-dl, a single string can also be used
    outtmpl_na_placeholder: Placeholder for unavailable meta fields.
    restrictfilenames: Do not allow "&" and spaces in file names
    trim_file_name:    Limit length of filename (extension excluded)
    windowsfilenames:  Force the filenames to be windows compatible
    ignoreerrors:      Do not stop on download/postprocessing errors.
                       Can be 'only_download' to ignore only download errors.
                       Default is 'only_download' for CLI, but False for API
    skip_playlist_after_errors: Number of allowed failures until the rest of
                       the playlist is skipped
    force_generic_extractor: Force downloader to use the generic extractor
    overwrites:        Overwrite all video and metadata files if True,
                       overwrite only non-video files if None
                       and don't overwrite any file if False
                       For compatibility with youtube-dl,
                       "nooverwrites" may also be used instead
    playliststart:     Playlist item to start at.
    playlistend:       Playlist item to end at.
    playlist_items:    Specific indices of playlist to download.
    playlistreverse:   Download playlist items in reverse order.
    playlistrandom:    Download playlist items in random order.
    matchtitle:        Download only matching titles.
    rejecttitle:       Reject downloads for matching titles.
    logger:            Log messages to a logging.Logger instance.
    logtostderr:       Log messages to stderr instead of stdout.
    consoletitle:       Display progress in console window's titlebar.
    writedescription:  Write the video description to a .description file
    writeinfojson:     Write the video description to a .info.json file
    clean_infojson:    Remove private fields from the infojson
    getcomments:       Extract video comments. This will not be written to disk
                       unless writeinfojson is also given
    writeannotations:  Write the video annotations to a .annotations.xml file
    writethumbnail:    Write the thumbnail image to a file
    allow_playlist_files: Whether to write playlists' description, infojson etc
                       also to disk when using the 'write*' options
    write_all_thumbnails:  Write all thumbnail formats to files
    writelink:         Write an internet shortcut file, depending on the
                       current platform (.url/.webloc/.desktop)
    writeurllink:      Write a Windows internet shortcut file (.url)
    writewebloclink:   Write a macOS internet shortcut file (.webloc)
    writedesktoplink:  Write a Linux internet shortcut file (.desktop)
    writesubtitles:    Write the video subtitles to a file
    writeautomaticsub: Write the automatically generated subtitles to a file
    allsubtitles:      Deprecated - Use subtitleslangs = ['all']
                       Downloads all the subtitles of the video
                       (requires writesubtitles or writeautomaticsub)
    listsubtitles:     Lists all available subtitles for the video
    subtitlesformat:   The format code for subtitles
    subtitleslangs:    List of languages of the subtitles to download (can be regex).
                       The list may contain "all" to refer to all the available
                       subtitles. The language can be prefixed with a "-" to
                       exclude it from the requested languages. Eg: ['all', '-live_chat']
    keepvideo:         Keep the video file after post-processing
    daterange:         A DateRange object, download only if the upload_date is in the range.
    skip_download:     Skip the actual download of the video file
    cachedir:          Location of the cache files in the filesystem.
                       False to disable filesystem cache.
    noplaylist:        Download single video instead of a playlist if in doubt.
    age_limit:         An integer representing the user's age in years.
                       Unsuitable videos for the given age are skipped.
    min_views:         An integer representing the minimum view count the video
                       must have in order to not be skipped.
                       Videos without view count information are always
                       downloaded. None for no limit.
    max_views:         An integer representing the maximum view count.
                       Videos that are more popular than that are not
                       downloaded.
                       Videos without view count information are always
                       downloaded. None for no limit.
    download_archive:  File name of a file where all downloads are recorded.
                       Videos already present in the file are not downloaded
                       again.
    break_on_existing: Stop the download process after attempting to download a
                       file that is in the archive.
    break_on_reject:   Stop the download process when encountering a video that
                       has been filtered out.
    cookiefile:        File name where cookies should be read from and dumped to
    cookiesfrombrowser: A tuple containing the name of the browser and the profile
                       name/path from where cookies are loaded.
                       Eg: ('chrome', ) or (vivaldi, 'default')
    nocheckcertificate:Do not verify SSL certificates
    prefer_insecure:   Use HTTP instead of HTTPS to retrieve information.
                       At the moment, this is only supported by YouTube.
    proxy:             URL of the proxy server to use
    geo_verification_proxy:  URL of the proxy to use for IP address verification
                       on geo-restricted sites.
    socket_timeout:    Time to wait for unresponsive hosts, in seconds
    bidi_workaround:   Work around buggy terminals without bidirectional text
                       support, using fridibi
    debug_printtraffic:Print out sent and received HTTP traffic
    include_ads:       Download ads as well
    default_search:    Prepend this string if an input url is not valid.
                       'auto' for elaborate guessing
    encoding:          Use this encoding instead of the system-specified.
    extract_flat:      Do not resolve URLs, return the immediate result.
                       Pass in 'in_playlist' to only show this behavior for
                       playlist items.
    postprocessors:    A list of dictionaries, each with an entry
                       * key:  The name of the postprocessor. See
                               yt_dlp/postprocessor/__init__.py for a list.
                       * when: When to run the postprocessor. Can be one of
                               pre_process|before_dl|post_process|after_move.
                               Assumed to be 'post_process' if not given
    post_hooks:        Deprecated - Register a custom postprocessor instead
                       A list of functions that get called as the final step
                       for each video file, after all postprocessors have been
                       called. The filename will be passed as the only argument.
    progress_hooks:    A list of functions that get called on download
                       progress, with a dictionary with the entries
                       * status: One of "downloading", "error", or "finished".
                                 Check this first and ignore unknown values.
                       * info_dict: The extracted info_dict
                       If status is one of "downloading", or "finished", the
                       following properties may also be present:
                       * filename: The final filename (always present)
                       * tmpfilename: The filename we're currently writing to
                       * downloaded_bytes: Bytes on disk
                       * total_bytes: Size of the whole file, None if unknown
                       * total_bytes_estimate: Guess of the eventual file size,
                                               None if unavailable.
                       * elapsed: The number of seconds since download started.
                       * eta: The estimated time in seconds, None if unknown
                       * speed: The download speed in bytes/second, None if
                                unknown
                       * fragment_index: The counter of the currently
                                         downloaded video fragment.
                       * fragment_count: The number of fragments (= individual
                                         files that will be merged)
                       Progress hooks are guaranteed to be called at least once
                       (with status "finished") if the download is successful.
    postprocessor_hooks:  A list of functions that get called on postprocessing
                       progress, with a dictionary with the entries
                       * status: One of "started", "processing", or "finished".
                                 Check this first and ignore unknown values.
                       * postprocessor: Name of the postprocessor
                       * info_dict: The extracted info_dict
                       Progress hooks are guaranteed to be called at least twice
                       (with status "started" and "finished") if the processing is successful.
    merge_output_format: Extension to use when merging formats.
    final_ext:         Expected final extension; used to detect when the file was
                       already downloaded and converted. "merge_output_format" is
                       replaced by this extension when given
    fixup:             Automatically correct known faults of the file.
                       One of:
                       - "never": do nothing
                       - "warn": only emit a warning
                       - "detect_or_warn": check whether we can do anything
                                           about it, warn otherwise (default)
    source_address:    Client-side IP address to bind to.
    call_home:         Boolean, true iff we are allowed to contact the
                       yt-dlp servers for debugging. (BROKEN)
    sleep_interval_requests: Number of seconds to sleep between requests
                       during extraction
    sleep_interval:    Number of seconds to sleep before each download when
                       used alone or a lower bound of a range for randomized
                       sleep before each download (minimum possible number
                       of seconds to sleep) when used along with
                       max_sleep_interval.
    max_sleep_interval:Upper bound of a range for randomized sleep before each
                       download (maximum possible number of seconds to sleep).
                       Must only be used along with sleep_interval.
                       Actual sleep time will be a random float from range
                       [sleep_interval; max_sleep_interval].
    sleep_interval_subtitles: Number of seconds to sleep before each subtitle download
    listformats:       Print an overview of available video formats and exit.
    list_thumbnails:   Print a table of all thumbnails and exit.
    match_filter:      A function that gets called with the info_dict of
                       every video.
                       If it returns a message, the video is ignored.
                       If it returns None, the video is downloaded.
                       match_filter_func in utils.py is one example for this.
    no_color:          Do not emit color codes in output.
    geo_bypass:        Bypass geographic restriction via faking X-Forwarded-For
                       HTTP header
    geo_bypass_country:
                       Two-letter ISO 3166-2 country code that will be used for
                       explicit geographic restriction bypassing via faking
                       X-Forwarded-For HTTP header
    geo_bypass_ip_block:
                       IP range in CIDR notation that will be used similarly to
                       geo_bypass_country
    The following options determine which downloader is picked:
    external_downloader: A dictionary of protocol keys and the executable of the
                       external downloader to use for it. The allowed protocols
                       are default|http|ftp|m3u8|dash|rtsp|rtmp|mms.
                       Set the value to 'native' to use the native downloader
    hls_prefer_native: Deprecated - Use external_downloader = {'m3u8': 'native'}
                       or {'m3u8': 'ffmpeg'} instead.
                       Use the native HLS downloader instead of ffmpeg/avconv
                       if True, otherwise use ffmpeg/avconv if False, otherwise
                       use downloader suggested by extractor if None.
    compat_opts:       Compatibility options. See "Differences in default behavior".
                       The following options do not work when used through the API:
                       filename, abort-on-error, multistreams, no-live-chat, format-sort
                       no-clean-infojson, no-playlist-metafiles, no-keep-subs.
                       Refer __init__.py for their implementation
    progress_template: Dictionary of templates for progress outputs.
                       Allowed keys are 'download', 'postprocess',
                       'download-title' (console title) and 'postprocess-title'.
                       The template is mapped on a dictionary with keys 'progress' and 'info'
    The following parameters are not used by YoutubeDL itself, they are used by
    the downloader (see yt_dlp/downloader/common.py):
    nopart, updatetime, buffersize, ratelimit, throttledratelimit, min_filesize,
    max_filesize, test, noresizebuffer, retries, fragment_retries, continuedl,
    noprogress, xattr_set_filesize, hls_use_mpegts, http_chunk_size,
    external_downloader_args.
    The following options are used by the post processors:
    prefer_ffmpeg:     If False, use avconv instead of ffmpeg if both are available,
                       otherwise prefer ffmpeg. (avconv support is deprecated)
    ffmpeg_location:   Location of the ffmpeg/avconv binary; either the path
                       to the binary or its containing directory.
    postprocessor_args: A dictionary of postprocessor/executable keys (in lower case)
                       and a list of additional command-line arguments for the
                       postprocessor/executable. The dict can also have "PP+EXE" keys
                       which are used when the given exe is used by the given PP.
                       Use 'default' as the name for arguments to passed to all PP
                       For compatibility with youtube-dl, a single list of args
                       can also be used
    The following options are used by the extractors:
    extractor_retries: Number of times to retry for known errors
    dynamic_mpd:       Whether to process dynamic DASH manifests (default: True)
    hls_split_discontinuity: Split HLS playlists to different formats at
                       discontinuities such as ad breaks (default: False)
    extractor_args:    A dictionary of arguments to be passed to the extractors.
                       See "EXTRACTOR ARGUMENTS" for details.
                       Eg: {'youtube': {'skip': ['dash', 'hls']}}
    youtube_include_dash_manifest: Deprecated - Use extractor_args instead.
                       If True (default), DASH manifests and related
                       data will be downloaded and processed by extractor.
                       You can reduce network I/O by disabling it if you don't
                       care about DASH. (only for youtube)
    youtube_include_hls_manifest: Deprecated - Use extractor_args instead.
                       If True (default), HLS manifests and related
                       data will be downloaded and processed by extractor.
                       You can reduce network I/O by disabling it if you don't
                       care about HLS. (only for youtube)'''