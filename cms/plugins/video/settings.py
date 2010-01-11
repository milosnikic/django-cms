from django.conf import settings

VIDEO_AUTOPLAY = getattr(settings, "VIDEO_AUTOPLAY", False)
VIDEO_AUTOHIDE = getattr(settings, "VIDEO_AUTOHIDE", False)
VIDEO_FULLSCREEN = getattr(settings, "VIDEO_FULLSCREEN", True)
VIDEO_LOOP = getattr(settings, "VIDEO_LOOP", False)
VIDEO_AUTOPLAY = getattr(settings, "VIDEO_AUTOPLAY", False)
VIDEO_AUTOPLAY = getattr(settings, "VIDEO_AUTOPLAY", False)

VIDEO_BG_COLOR = getattr(settings, "VIDEO_BG_COLOR", "000000")
VIDEO_TEXT_COLOR = getattr(settings, "VIDEO_TEXT_COLOR", "FFFFFF")
VIDEO_SEEKBAR_COLOR = getattr(settings, "VIDEO_SEEKBAR_COLOR", "13ABEC")
VIDEO_SEEKBARBG_COLOR = getattr(settings, "VIDEO_SEEKBARBG_COLOR", "333333")
VIDEO_LOADINGBAR_COLOR = getattr(settings, "VIDEO_LOADINGBAR_COLOR", "828282")
VIDEO_BUTTON_OUT_COLOR = getattr(settings, "VIDEO_BUTTON_OUT_COLOR", "333333")
VIDEO_BUTTON_OVER_COLOR = getattr(settings, "VIDEO_BUTTON_OVER_COLOR", "000000")
VIDEO_BUTTON_HIGHLIGHT_COLOR = getattr(settings, "VIDEO_BUTTON_HIGHLIGHT_COLOR", "FFFFFF")
