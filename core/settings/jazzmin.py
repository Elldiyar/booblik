JAZZMIN_SETTINGS = {
    "site_title": "Booblik",
    "site_header": "Booblik",
    "site_logo_classes": "img-circle",
    "site_brand": "Админ-панель",
    "welcome_sign": "Добро пожаловать в Booblik",
    "copyright": "Booblik",
    "search_model": ["auth.User"],
    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "Booblik"},
        {"model": "auth.User"},
    ],
    "default_icon_parents": "fas fa-circle",
    "default_icon_children": "fas fa-dot-circle",
    "show_sidebar": True,
    "navigation_expanded": True,
    "changeform_format": "horizontal_tabs",
    "language_chooser": False,
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "icons": {
        "vacancy.Vacancy": "fas fa-solid fa-briefcase",
        "filial.Filial": "fas fa-solid fa-map",
        "filial.Contact": "fas fa-solid fa-address-book",
        "filial.Image": "fas fa-solid fa-image",
        "filial.Music": "fas fa-solid fa-music",
        "filial.AboutMe": "fas fa-solid fa-info",
        "filial.AboutMeFact": "fas fa-solid fa-question",
        "courses.Review": "fas fa-solid fa-comment",
        "event.Event": "fas fa-solid fa-image",
        "event.News": "fas fa-thin fa-newspaper",
        "menu.Menu": "fas fa-solid fa-bars",
        "menu.Product": "fas fa-solid fa-cookie-bite",
        "auth.Group": "fas fa-users",
        "auth.User": "fas fa-user",
    }
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
    "actions_sticky_top": True,
}
