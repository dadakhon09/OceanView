class Icons:
    def get_icons(self):
        icons_list = (
            (0, 'beach-slipper'),
            (1, 'bus-ticket'),
            (2, 'cocktail'),
            (3, 'compass-alt'),
            (4, 'apple'),
            (5, 'bower'),
            (6, 'delicious'),
            (7, 'messenger'),
            (8, 'meteor'),
            (9, 'netflix'),
            (10, 'nginx'),
            (11, 'onenote'),
            (12, 'onedrive'),
            (12, 'redis'),
            (13, 'shopify'),
            (14, 'shazam'),
            (15, 'telegram'),
            (16, 'facebook'),
            (17, 'twitter'),
            (18, 'yandex'),
            (19, 'atom'),
            (20, 'angelist'),
            (21, 'vk'),
            (22, 'bluetooth-b'),
            (23, 'dribbble'),
            (24, 'google'),
            (25, 'hangout'),
            (26, 'linux'),
            (27, 'playstation'),
            (28, 'steam'),
            (29, 'wifi-logo'),
            (30, 'wikipedia'),
            (31, 'windows'),
            (32, 'xbox'),
            (33, 'fontisto'),
            (34, 'instagram'),
            (35, 'youtube-play'),
            (36, 'chrome'),
            (37, 'blind'),
            (38, 'deaf'),
            (39, 'universal-access'),
            (40, 'low-vision'),
            (41, 'tty'),
            (42, 'wheelchair'),
            (43, 'pie-chart-2'),
            (44, 'line-chart'),
            (45, 'dollar'),
            (46, 'arrow-swap'),
            (47, 'arrow-move'),
            (48, 'arrow-return-right'),
            (49, 'arrow-return-left'),
            (50, 'checkbox-active'),
            (51, 'like'),
            (52, 'dislike'),
            (53, 'visa'),
            (54, 'mastercard'),
            (55, 'paypal'),
            (56, 'play'),
            (57, 'pause'),
            (58, 'equalizer'),
            (59, 'heart'),
            (60, 'headphone'),
            (61, 'mic'),
            (62, 'music-note'),
            (63, 'player-settings'),
            (64, 'star'),
            (65, 'automobile'),
            (66, 'bicycle'),
            (67, 'bus'),
            (68, 'car'),
            (69, 'helicopter'),
            (70, 'metro'),
            (71, 'motorcycle'),
            (72, 'plane'),
            (73, 'rocket'),
            (74, 'ship'),
            (75, 'subway'),
            (76, 'taxi'),
            (77, 'train'),
            (78, 'truck'),
            (79, 'yacht'),
            (80, 'direction-sign'),
            (81, 'holiday-village'),
            (82, 'hot-air-balloon'),
            (83, 'hotel-alt'),
            (84, 'hotel'),
            (85, 'island'),
            (86, 'money-symbol'),
            (87, 'parasol'),
            (88, 'passport'),
            (89, 'passport-alt'),
            (90, 'photograph'),
            (91, 'plane-ticket'),
            (92, 'room'),
            (93, 'sait-boat'),
            (94, 'suitcase'),
            (95, 'sun'),
            (96, 'sunglasses'),
            (97, 'swimsuit'),
            (98, 'tent'),
            (99, 'train-ticket'),
            (100, 'wallet'),
            (101, 'language'),
            (102, 'archive'),
            (103, 'at'),
            (104, 'ban'),
            (105, 'bell'),
            (106, 'bell-alt'),
            (107, 'bookmark'),
            (108, 'bookmark-alt'),
            (109, 'bug'),
            (110, 'calculator'),
            (111, 'calendar'),
            (112, 'desktop'),
            (113, 'download'),
            (114, 'film'),
            (115, 'history'),
            (116, 'hourglass-end'),
            (117, 'info'),
            (118, 'key'),
            (119, 'keyboard'),
            (120, 'laptop'),
            (121, 'lightbulb'),
            (122, 'magnet'),
            (123, 'map-marker-alt'),
            (124, 'map-marker'),
            (125, 'map'),
            (126, 'mobile-alt'),
            (127, 'paw'),
            (128, 'phone'),
            (129, 'power'),
            (130, 'qrcode'),
            (131, 'question'),
            (132, 'search'),
            (133, 'sitemap'),
            (134, 'stopwatch'),
            (135, 'ticket'),
            (136, 'user-secret'),
            (137, 'camera'),
            (138, 'clock'),
            (139, 'code'),
            (140, 'comment'),
            (141, 'commenting'),
            (142, 'comments'),
            (143, 'crop'),
            (144, 'cursor'),
            (145, 'database'),
            (146, 'date'),
            (147, 'earth'),
            (148, 'email'),
            (149, 'eye'),
            (150, 'female'),
            (151, 'filter'),
            (152, 'fire'),
            (153, 'flag'),
            (154, 'flash'),
            (155, 'home'),
            (156, 'link'),
            (157, 'locked'),
            (158, 'male'),
            (159, 'more-v-a'),
            (160, 'nav-icon-grid-a'),
            (161, 'navigate'),
            (162, 'paper-plane'),
            (163, 'person'),
            (164, 'persons'),
            (165, 'picture'),
            (166, 'plus'),
            (167, 'plus-a'),
            (168, 'print'),
            (169, 'quote-a-left'),
            (170, 'quote-a-right'),
            (171, 'quote-right'),
            (172, 'quote-left'),
            (173, 'rss'),
            (174, 'scissors'),
            (175, 'share'),
            (176, 'trash'),
            (177, 'unlocked'),
            (178, 'usb'),
            (179, 'wifi'),
            (180, 'world-o'),
            (181, 'world'),
            (182, 'zoom'),
            (183, 'recycle'),
            (184, 'check'),
            (185, 'asterisk'),
            (186, 'hashtag'),
            (187, 'pinboard'),
            (188, 'table-1'),
            (189, 'table-2'),
            (190, 'undo'),
            (191, 'cloud-up'),
            (192, 'cloud-down'),
            (193, 'cloudy'),
            (194, 'cloudy-gusts'),
            (195, 'compass'),
            (196, 'day-cloudy'),
            (197, 'day-lightning'),
            (198, 'day-rain'),
            (199, 'day-snow'),
            (200, 'day-sunny'),
            (201, 'fog'),
            (202, 'thermometer'),
            (203, 'umbrella'),
            (204, 'wind'),
            (205, 'rainbow'),
            (206, 'smiley'),
            (207, 'ambulance'),
            (208, 'aids'),
            (209, 'bed-patient'),
            (210, 'bandage'),
            (211, 'blood'),
            (212, 'dna'),
            (213, 'doctor'),
            (214, 'first-aid-alt'),
            (215, 'heart-alt'),
            (216, 'hospital'),
            (217, 'nurse'),
            (218, 'pills'),
            (219, 'prescription'),
            (220, 'pulse-alt'),
            (221, 'thermometer-alt'),
            (222, 'test-tube'),
            (223, 'snow-flake'),
            (224, 'shopping-bag'),
            (225, 'shopping-basket'),
            (226, 'shopping-package'),
            (227, 'shopping-sale'),
            (228, 'shopping-store'),
            (229, 'shopping-barcode'),
        )

        return icons_list
