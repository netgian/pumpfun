from .client import client


def hello_world() -> str:
    """Return a greeting."""
    return client.request(
        method="GET",
        endpoint="/"
    )


def get_health() -> dict:
    """Check the health of the API."""
    return client.request(
        method="GET",
        endpoint="/health"
    )


def get_latest_trades() -> dict:
    """Return the latest trades."""
    return client.request(
        method="GET",
        endpoint="/trades/latest"
    )


def get_all_trades(mint: str, limit: int, offset: int = 0, minimum_size: int = 0) -> dict:
    """Return all trades for a given mint."""
    return client.request(
        method="GET",
        endpoint=f"/trades/all/{mint}",
        params={
            "limit": limit,
            "offset": offset,
            "minimumSize": minimum_size
        }
    )


# def create_trade_signature() -> dict:
#     """Create a trade signature."""
#     return client.request(
#         method="POST",
#         endpoint="/trades/signatures"
#     )


# def create_small_trade_signature() -> dict:
#     """Create a trade signature."""
#     return client.request(
#         method="POST",
#         endpoint="/trades/signatures/small"
#     )


def get_trade_count(mint: str, minimum_size: int = 0) -> dict:
    """Return the number of trades for a given mint."""
    return client.request(
        method="GET",
        endpoint=f"/trades/count/{mint}",
        params={
            "minimumSize": minimum_size
        }
    )


def get_trades_follows_user(mint: str, follows_user_id: str, limit: int, offset: int = 0, minimum_size: int = 0) -> dict:
    """Return trades for a given mint filtered by a following user ID."""
    return client.request(
        method="GET",
        endpoint=f"/trades/followsUserId/{mint}",
        params={
            "followsUserId": follows_user_id,
            "limit": limit,
            "offset": offset,
            "minimumSize": minimum_size
        }
    )


def get_trades_follows_user_count(mint: str, follows_user_id: str, minimum_size: int = 0) -> dict:
    """Return the count of trades for a given mint filtered by a following user ID."""
    return client.request(
        method="GET",
        endpoint=f"/trades/followsUserId/count/{mint}",
        params={
            "followsUserId": follows_user_id,
            "minimumSize": minimum_size,
        }
    )


# def sign_create_coin_tx() -> dict:
#     """Create a sign transaction."""
#     return client.request(
#         method="POST",
#         endpoint="/coins/sign-create-tx"
#     )


# def create_coin() -> dict:
#     """Create a coin."""
#     return client.request(
#         method="POST",
#         endpoint="/coins/create"
#     )


# def get_top_runners(data: list) -> dict:
#     """Get top runners."""
#     return client.request(
#         method="POST",
#         endpoint="/coins/top-runners",
#         json=data
#     )


def get_top_runners() -> dict:
    """Get top runners."""
    return client.request(
        method="GET",
        endpoint="/coins/top-runners"
    )


def get_king_of_the_hill(include_nsfw: str = "") -> dict:
    """Get king of the hill."""
    return client.request(
        method="GET",
        endpoint="/coins/king-of-the-hill",
        params={
            "includeNsfw": include_nsfw
        }
    )


def get_currently_live(limit: int, offset: int = 0, include_nsfw: bool = True) -> dict:
    """Get currently live coins."""
    return client.request(
        method="GET",
        endpoint="/coins/currently-live",
        params={
            "limit": limit,
            "offset": offset,
            "includeNsfw": str(include_nsfw).lower()
        }
    )


def get_coins_for_you(limit: int, offset: int = 0, include_nsfw: bool = True) -> dict:
    """Get coins for you."""
    return client.request(
        method="GET",
        endpoint="/coins/for-you",
        params={
            "limit": limit,
            "offset": offset,
            "includeNsfw": str(include_nsfw).lower()
        }
    )


def get_featured_coins(time_window: str, limit: int, offset: int = 0, include_nsfw: bool = True) -> dict:
    """Get featured coins for a given time window."""
    return client.request(
        method="GET",
        endpoint=f"/coins/featured/{time_window}",
        params={
            "limit": limit,
            "offset": offset,
            "includeNsfw": str(include_nsfw).lower()
        }
    )


def get_user_created_coins(user_id: str, limit: int, offset: int = 0) -> dict:
    """Get coins created by a specific user."""
    return client.request(
        method="GET",
        endpoint=f"/coins/user-created-coins/{user_id}",
        params={
            "limit": limit,
            "offset": offset
        }
    )


def get_default_bookmarks(limit: int, offset: int = 0, include_nsfw: bool = True) -> dict:
    """Get default bookmarks."""
    return client.request(
        method="GET",
        endpoint="/coins/bookmarks/default",
        params={
            "limit": limit,
            "offset": offset,
            "includeNsfw": str(include_nsfw).lower()
        }
    )


def get_bookmarks_by_id(bookmark_id: str, limit: int, offset: int = 0, include_nsfw: bool = True) -> dict:
    """Get bookmarks by ID."""
    return client.request(
        method="GET",
        endpoint=f"/coins/bookmarks/{bookmark_id}",
        params={
            "limit": limit,
            "offset": offset,
            "includeNsfw": str(include_nsfw).lower()
        }
    )


def check_free_coin(mint: str) -> dict:
    """Check if a coin is free."""
    return client.request(
        method="GET",
        endpoint=f"/coins/is-free-coin/{mint}"
    )


def get_latest_coins() -> dict:
    """Get the latest coins."""
    return client.request(
        method="GET",
        endpoint="/coins/latest"
    )


def get_protected_coins(limit: int, offset: int, sort: str, search_term: str, order: str, include_nsfw: str,
                        creator: str, complete: str, is_live: str, from_date: str, to_date: str, banned: str) -> dict:
    """Get protected coins."""
    return client.request(
        method="GET",
        endpoint="/coins/protected",
        params={
            "limit": limit,
            "offset": offset,
            "sort": sort,
            "searchTerm": search_term,
            "order": order,
            "includeNsfw": include_nsfw,
            "creator": creator,
            "complete": complete,
            "isLive": is_live,
            "fromDate": from_date,
            "toDate": to_date,
            "banned": banned
        }
    )


def get_personalized_coins(user_id: str) -> dict:
    """Get personalized coins for a specific user."""
    return client.request(
        method="GET",
        endpoint="/coins/personalized",
        params={
            "userId": user_id
        }
    )


def get_similar_coins(mint: str, limit: int) -> dict:
    """Get similar coins."""
    return client.request(
        method="GET",
        endpoint="/coins/similar",
        params={
            "mint": mint,
            "limit": limit
        }
    )


# def create_mint() -> dict:
#     """Create a new mint."""
#     return client.request(
#         method="POST",
#         endpoint="/coins/mints"
#     )


def search_coins(limit: int, offset: int, sort: str, search_term: str, order: str, include_nsfw: bool,
                 creator: str,complete: bool, meta: str, coin_type: str) -> dict:
    """Search for coins."""
    return client.request(
        method="GET",
        endpoint="/coins/search",
        params={
            "limit": limit,
            "offset": offset,
            "sort": sort,
            "searchTerm": search_term,
            "order": order,
            "includeNsfw": str(include_nsfw).lower(),
            "creator": creator,
            "complete": str(complete).lower(),
            "meta": meta,
            "type": coin_type
        }
    )


def get_coin(mint: str, sync: bool=True) -> dict:
    """Get a specific coin by mint."""
    return client.request(
        method="GET",
        endpoint=f"/coins/{mint}",
        params={
            "sync": str(sync).lower()
        }
    )


def get_coins(limit: int, offset: int, sort: str, search_term: str, order: str,
              include_nsfw: bool, creator: str, complete: bool, meta: str) -> dict:
    """Get coins."""
    return client.request(
        method="GET",
        endpoint="/coins",
        params={
            "limit": limit,
            "offset": offset,
            "sort": sort,
            "searchTerm": search_term,
            "order": order,
            "includeNsfw": str(include_nsfw).lower(),
            "creator": creator,
            "complete": str(complete).lower(),
            "meta": meta
        }
    )


# def ban_coin(mint: str) -> dict:
#     """Ban a specific coin by mint."""
#     return client.request(
#         method="PATCH",
#         endpoint=f"/coins/ban/{mint}"
#     )


def get_sol_price() -> dict:
    """Get the current SOL price."""
    return client.request(
        method="GET",
        endpoint="/sol-price"
    )


def is_admin() -> str:
    """Check if the user is an admin."""
    return client.request(
        method="GET",
        endpoint="/auth/is-admin"
    )


def is_super_admin() -> dict:
    """Check if the user is a super admin."""
    return client.request(
        method="GET",
        endpoint="/auth/is-super-admin"
    )


# def login() -> dict:
#     """Login a user."""
#     return client.request(
#         method="POST",
#         endpoint="/auth/login",
#     )


def get_my_profile() -> dict:
    """Get the profile of the authenticated user."""
    return client.request(
        method="GET",
        endpoint="/auth/my-profile"
    )


def is_valid_jurisdiction() -> dict:
    """Check if the user's jurisdiction is valid."""
    return client.request(
        method="GET",
        endpoint="/auth/is-valid-jurisdiction"
    )


# def logout() -> dict:
#     """Logout a user."""
#     return client.request(
#         method="POST",
#         endpoint="/auth/logout"
#     )


def check_address(address: str) -> dict:
    """Check the validity of an address."""
    return client.request(
        method="GET",
        endpoint=f"/check/{address}"
    )


def get_moderation_logs(offset: int, limit: int, moderator: str) -> dict:
    """Get moderation logs."""
    return client.request(
        method="GET",
        endpoint="/moderation/logs",
        params={
            "offset": offset,
            "limit": limit,
            "moderator": moderator
        }
    )


# def ban_address(address: str) -> dict:
#     """Ban a specific address."""
#     return client.request(
#         method="POST",
#         endpoint=f"/moderation/ban/address/{address}"
#     )


# def mark_as_nsfw(mint: str) -> dict:
#     """Mark a specific mint as NSFW."""
#     return client.request(
#         method="POST",
#         endpoint=f"/moderation/mark-as-nsfw/{mint}"
#     )


# def mark_bulk_as_nsfw() -> dict:
#     """Mark multiple items as NSFW."""
#     return client.request(
#         method="POST",
#         endpoint="/moderation/bulk-nsfw"
#     )


# def mark_as_hidden(identification: int) -> dict:
#     """Mark a specific item as hidden."""
#     return client.request(
#         method="POST",
#         endpoint=f"/moderation/mark-as-hidden/{identification}"
#     )


# def mark_bulk_as_hidden() -> dict:
#     """Mark multiple items as hidden."""
#     return client.request(
#         method="POST",
#         endpoint="/moderation/bulk-hidden"
#     )


# def ban_item(identification: int) -> dict:
#     """Ban a specific item by ID."""
#     return client.request(
#         method="POST",
#         endpoint=f"/moderation/ban/{identification}"
#     )


# def ban_bulk_items() -> dict:
#     """Ban multiple items."""
#     return client.request(
#         method="POST",
#         endpoint="/moderation/bulk-ban"
#     )


# def ban_terms() -> dict:
#     """Ban terms."""
#     return client.request(
#         method="POST",
#         endpoint="/moderation/ban-terms"
#     )


def get_ban_terms() -> dict:
    """Get banned terms."""
    return client.request(
        method="GET",
        endpoint="/moderation/ban-terms"
    )


# def ban_image_terms() -> dict:
#     """Ban image terms."""
#     return client.request(
#         method="POST",
#         endpoint="/moderation/ban-image-terms"
#     )


def get_ban_image_terms() -> dict:
    """Get banned image terms."""
    return client.request(
        method="GET",
        endpoint="/moderation/ban-image-terms"
    )


# def ban_regex_patterns() -> dict:
#     """Ban regex patterns."""
#     return client.request(
#         method="POST",
#         endpoint="/moderation/ban-regex-patterns"
#     )


def get_ban_regex_patterns() -> dict:
    """Get banned regex patterns."""
    return client.request(
        method="GET",
        endpoint="/moderation/ban-regex-patterns"
    )


# def add_throttle_exception() -> dict:
#     """Add a throttle exception."""
#     return client.request(
#         method="POST",
#         endpoint="/moderation/add-throttle-exception"
#     )


def get_throttle_exceptions() -> dict:
    """Get throttle exceptions."""
    return client.request(
        method="GET",
        endpoint="/moderation/throttle-exceptions"
    )


# def delete_ban_term(identification: str) -> dict:
#     """Delete a banned term by ID."""
#     return client.request(
#         method="DELETE",
#         endpoint=f"/moderation/ban-terms/{identification}"
#     )


# def delete_ban_image_term(identification: str) -> dict:
#     """Delete a banned image term by ID."""
#     return client.request(
#         method="DELETE",
#         endpoint=f"/moderation/ban-image-terms/{identification}"
#     )


# def delete_ban_regex_pattern(identification: str) -> dict:
#     """Delete a banned regex pattern by ID."""
#     return client.request(
#         method="DELETE",
#         endpoint=f"/moderation/ban-regex-patterns/{identification}"
#     )


# def delete_throttle_exception(identification: str) -> dict:
#     """Delete a throttle exception by ID."""
#     return client.request(
#         method="DELETE",
#         endpoint=f"/moderation/delete-throttle-exception/{identification}"
#     )


def get_ban(identification: int) -> dict:
    """Get a ban by ID."""
    return client.request(
        method="GET",
        endpoint=f"/moderation/ban/{identification}"
    )


def get_ban_users(limit: str, offset: str, sort_by: str, order: str, search_query: str,
                  active: str, unban_request: str, from_date: str, to_date: str) -> dict:
    """Get banned users with specified query parameters."""
    return client.request(
        method="GET",
        endpoint="/moderation/ban-users",
        params={
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "searchQuery": search_query,
            "active": active,
            "unbanRequest": unban_request,
            "fromDate": from_date,
            "toDate": to_date
        }
    )


def get_moderated_comments(limit: int, group_number: int, next_token: str, show_non_spam: bool, status_filters: list) -> dict:
    """Get moderated comments with specified query parameters."""
    return client.request(
        method="GET",
        endpoint="/moderation/moderated-comments",
        params={
            "limit": limit,
            "groupNumber": group_number,
            "nextToken": next_token,
            "showNonSpam": str(show_non_spam).lower(),
            "statusFilters": status_filters
        }
    )


def get_moderated_reports(limit: int, group_number: int, next_token: str, show_non_spam: bool, status_filters: list) -> dict:
    """Get moderated reports with specified query parameters."""
    return client.request(
        method="GET",
        endpoint="/moderation/moderated-reports",
        params={
            "limit": limit,
            "groupNumber": group_number,
            "nextToken": next_token,
            "showNonSpam": str(show_non_spam).lower(),
            "statusFilters": status_filters
        }
    )


# def mark_as_ignored(identification: int) -> dict:
#     """Mark a moderation item as ignored by ID."""
#     return client.request(
#         method="POST",
#         endpoint=f"/moderation/mark-as-ignored/{identification}"
#     )


# def delete_photo(mint: str) -> dict:
#     """Delete a photo by mint."""
#     return client.request(
#         method="POST",
#         endpoint=f"/moderation/delete-photo/{mint}"
#     )


def get_vanity_key(captcha_token: str) -> dict:
    """Get a vanity key with the specified captcha token."""
    return client.request(
        method="GET",
        endpoint="/vanity/key",
        params={
            "captchaToken": captcha_token
        }
    )


def get_random_mint_public_key() -> dict:
    """Get a random mint public key."""
    return client.request(
        method="GET",
        endpoint="/vanity/random-mint-public-key"
    )


def get_current_metas() -> dict:
    """Get current metas."""
    return client.request(
        method="GET",
        endpoint="/metas/current"
    )


def search_metas(meta: str, include_nsfw: bool) -> dict:
    """Search metas with the specified meta and include NSFW flag."""
    return client.request(
        method="GET",
        endpoint="/metas/search",
        params={
            "meta": meta,
            "includeNsfw": str(include_nsfw).lower()
        }
    )


# def post_reply(data: dict) -> dict:
#     """Post a reply with the specified data."""
#     return client.request(
#         method="POST",
#         endpoint="/replies",
#         json=data
#     )


def get_replies(limit: int, offset: int) -> dict:
    """Get replies with the specified limit and offset."""
    return client.request(
        method="GET",
        endpoint="/replies",
        params={
            "limit": limit,
            "offset": offset
        }
    )


def get_banned_replies() -> dict:
    """Get banned replies."""
    return client.request(
        method="GET",
        endpoint="/replies/ban"
    )


def get_protected_replies(limit: str, offset: str, sort_by: str, order: str, address: str,search_query: str,
                          search_ca: str, search_ua: str, hidden: str, banned: str, from_date: str, to_date: str,
                          has_image: str, is_scam: str, is_spam: str) -> dict:
    """Get protected replies with specified query parameters."""
    return client.request(
        method="GET",
        endpoint="/replies/protected-replies",
        params={
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "address": address,
            "searchQuery": search_query,
            "searchCA": search_ca,
            "searchUA": search_ua,
            "hidden": hidden,
            "banned": banned,
            "fromDate": from_date,
            "toDate": to_date,
            "hasImage": has_image,
            "isScam": is_scam,
            "isSpam": is_spam
        }
    )


def get_replies_by_mint(mint: str, limit: int, offset: int, user: str, reverse_order: bool) -> dict:
    """Get replies for a specific mint with specified query parameters."""
    return client.request(
        method="GET",
        endpoint=f"/replies/{mint}",
        params={
            "limit": limit,
            "offset": offset,
            "user": user,
            "reverseOrder": str(reverse_order).lower()
        }
    )


# def post_replies_by_mints(data: dict) -> dict:
#     """Post replies for multiple mints with the specified data."""
#     return client.request(
#         method="POST",
#         endpoint="/replies/mints",
#         json=data
#     )


def get_user_replies(address: str, limit: int, offset: int) -> dict:
    """Get replies for a specific user address with specified query parameters."""
    return client.request(
        method="GET",
        endpoint=f"/replies/user-replies/{address}",
        params={
            "limit": limit,
            "offset": offset
        }
    )


def is_origin_of_reply_banned(identification: int) -> dict:
    """Check if the origin of a reply is banned by ID."""
    return client.request(
        method="GET",
        endpoint=f"/replies/is-origin-of-reply-banned/{identification}"
    )


# def post_experimental_replies(data: dict) -> dict:
#     """Post experimental replies with the specified data."""
#     return client.request(
#         method="POST",
#         endpoint="/replies/experimental",
#         json=data
#     )


def get_notifications(limit: int, offset: int) -> dict:
    """Get notifications with the specified limit and offset."""
    return client.request(
        method="GET",
        endpoint="/notifications",
        params={
            "limit": limit,
            "offset": offset
        }
    )


def search_users(search_term: str, offset: int, limit: int, sort: str, order: str) -> dict:
    """Search for users with the specified query parameters."""
    return client.request(
        method="GET",
        endpoint="/users/search",
        params={
            "searchTerm": search_term,
            "offset": offset,
            "limit": limit,
            "sort": sort,
            "order": order
        }
    )


# def post_users_batch(data: dict) -> dict:
#     """Post a batch of users with the specified data."""
#     return client.request(
#         method="POST",
#         endpoint="/users/batch",
#         json=data
#     )


def get_user_by_id(user_id: str) -> dict:
    """Get a user by their ID."""
    return client.request(
        method="GET",
        endpoint=f"/users/{user_id}"
    )


# def post_user_register(data: dict) -> dict:
#     """Register a new user with the specified data."""
#     return client.request(
#         method="POST",
#         endpoint="/users/register",
#         json=data
#     )


# def post_user(data: dict) -> dict:
#     """Create a new user with the specified data."""
#     return client.request(
#         method="POST",
#         endpoint="/users",
#         json=data
#     )


# def delete_users() -> dict:
#     """Delete all users."""
#     return client.request(
#         method="DELETE",
#         endpoint="/users"
#     )


def get_candlesticks(mint: str, offset: int, limit: int, timeframe: int) -> dict:
    """Get candlesticks for a specific mint with specified query parameters."""
    return client.request(
        method="GET",
        endpoint=f"/candlesticks/{mint}",
        params={
            "offset": offset,
            "limit": limit,
            "timeframe": timeframe
        }
    )


def get_global_params(timestamp: int) -> dict:
    """Get global parameters for a specific timestamp."""
    return client.request(
        method="GET",
        endpoint=f"/global-params/{timestamp}"
    )


# def post_balances_index(data: dict) -> dict:
#     """Post balances index with the specified data."""
#     return client.request(
#         method="POST",
#         endpoint="/balances/index",
#         json=data
#     )


# def post_balances_index_all() -> dict:
#     """Post balances index for all."""
#     return client.request(
#         method="POST",
#         endpoint="/balances/index-all"
#     )


def get_balances(address: str, offset: int, limit: int, min_balance: int) -> dict:
    """Get balances for a specific address with specified query parameters."""
    return client.request(
        method="GET",
        endpoint=f"/balances/{address}",
        params={
            "offset": offset,
            "limit": limit,
            "minBalance": min_balance
        }
    )


# def post_likes(target_id: str) -> dict:
#     """Post a like for a specific target ID."""
#     return client.request(
#         method="POST",
#         endpoint=f"/likes/{target_id}"
#     )


# def delete_likes(target_id: str) -> dict:
#     """Delete a like for a specific target ID."""
#     return client.request(
#         method="DELETE",
#         endpoint=f"/likes/{target_id}"
#     )


def get_likes(target_id: str) -> dict:
    """Get likes for a specific target ID."""
    return client.request(
        method="GET",
        endpoint=f"/likes/{target_id}"
    )


# def post_send_transaction() -> dict:
#     """Send a transaction."""
#     return client.request(
#         method="POST",
#         endpoint="/send-transaction"
#     )


# def post_check_signatures() -> dict:
#     """Check signatures for a transaction."""
#     return client.request(
#         method="POST",
#         endpoint="/send-transaction/check-signatures"
#     )


def get_jito_tip_account() -> dict:
    """Get the Jito tip account."""
    return client.request(
        method="GET",
        endpoint="/send-transaction/jito-tip-account"
    )


# def post_following(user_id: str, captcha_token: str) -> dict:
#     """Follow a user with the specified user ID and captcha token."""
#     return client.request(
#         method="POST",
#         endpoint=f"/following/{user_id}",
#         params={
#             "captchaToken": captcha_token
#         }
#     )


# def delete_following(user_id: str) -> dict:
#     """Unfollow a user with the specified user ID."""
#     return client.request(
#         method="DELETE",
#         endpoint=f"/following/{user_id}"
#     )


def get_following(user_id: str) -> dict:
    """Get the following list for a specific user ID."""
    return client.request(
        method="GET",
        endpoint=f"/following/{user_id}"
    )


# def post_following_v2(user_id: str) -> dict:
#     """Follow a user with the specified user ID (version 2)."""
#     return client.request(
#         method="POST",
#         endpoint=f"/following/v2/{user_id}"
#     )


def get_following_single(identification: str, user_id: str) -> dict:
    """Get a single following entry by ID and user ID."""
    return client.request(
        method="GET",
        endpoint=f"/following/single/{identification}",
        params={
            "userId": user_id
        }
    )


def get_followers(identification: str) -> dict:
    """Get the followers list for a specific user ID."""
    return client.request(
        method="GET",
        endpoint=f"/following/followers/{identification}"
    )


def get_mutuals(identification: str) -> dict:
    """Get the mutual followers list for a specific user ID."""
    return client.request(
        method="GET",
        endpoint=f"/following/mutuals/{identification}"
    )


def get_timeline(user_id: str) -> dict:
    """Get the timeline for a specific user ID."""
    return client.request(
        method="GET",
        endpoint=f"/timeline/{user_id}"
    )


# def post_add_click(feed_id: str) -> dict:
#     """Add a click to a specific feed by feed ID."""
#     return client.request(
#         method="POST",
#         endpoint=f"/feed/add-click/{feed_id}"
#     )


# def post_add_load(feed_id: str) -> dict:
#     """Add a load to a specific feed by feed ID."""
#     return client.request(
#         method="POST",
#         endpoint=f"/feed/add-load/{feed_id}"
#     )


def get_livestreams(mint: str) -> dict:
    """Get the livestreams for a specific mint."""
    return client.request(
        method="GET",
        endpoint=f"/livestreams/{mint}"
    )


def get_livestreams_raw(mint: str) -> dict:
    """Get the raw livestreams for a specific mint."""
    return client.request(
        method="GET",
        endpoint=f"/livestreams/{mint}/raw"
    )


def get_livestreams_livekit_token_host(mint: str, creator: str) -> dict:
    """Get the LiveKit token for a host for a specific mint and creator."""
    return client.request(
        method="GET",
        endpoint="/livestreams/livekit/token/host",
        params={
            "mint": mint,
            "creator": creator
        }
    )


def get_livestreams_livekit_token_participant(mint: str, hidden: bool) -> dict:
    """Get the LiveKit token for a participant for a specific mint and hidden status."""
    return client.request(
        method="GET",
        endpoint="/livestreams/livekit/token/participant",
        params={
            "mint": mint,
            "hidden": str(hidden).lower()
        }
    )


# def post_livestreams_livekit_raise_hand(mint: str) -> dict:
#     """Raise hand in a LiveKit livestream for a specific mint."""
#     return client.request(
#         method="POST",
#         endpoint="/livestreams/livekit/raise-hand",
#         params={
#             "mint": mint
#         }
#     )


# def post_livestreams_livekit_invite_to_stage(mint: str) -> dict:
#     """Invite to stage in a LiveKit livestream for a specific mint."""
#     return client.request(
#         method="POST",
#         endpoint="/livestreams/livekit/invite-to-stage",
#         params={
#             "mint": mint
#         }
#     )


# def post_livestreams_livekit_remove_from_stage(mint: str) -> dict:
#     """Remove from stage in a LiveKit livestream for a specific mint."""
#     return client.request(
#         method="POST",
#         endpoint="/livestreams/livekit/remove-from-stage",
#         params={
#             "mint": mint
#         }
#     )


def get_livestreams_stream_livestream_token(creator: str) -> dict:
    """Get the livestream token for a specific creator."""
    return client.request(
        method="GET",
        endpoint="/livestreams/stream/livestream-token",
        params={
            "creator": creator
        }
    )


def get_livestreams_stream_livechat_token(user_id: str) -> dict:
    """Get the livechat token for a specific user ID."""
    return client.request(
        method="GET",
        endpoint="/livestreams/stream/livechat-token",
        params={
            "userId": user_id
        }
    )


# def post_livestreams_stream_livechat_channel(mint: str) -> dict:
#     """Create a livechat channel for a specific mint."""
#     return client.request(
#         method="POST",
#         endpoint=f"/livestreams/stream/livechat-channel/{mint}"
#     )


# def post_livestreams_create_livestream() -> dict:
#     """Create a new livestream."""
#     return client.request(
#         method="POST",
#         endpoint="/livestreams/create-livestream",
#         json={}
#     )


# def put_livestreams_update_livestream(data: dict) -> dict:
#     """Update an existing livestream."""
#     return client.request(
#         method="PUT",
#         endpoint="/livestreams/update-livestream",
#         json=data
#     )


# def put_livestreams_disable_livestream(mint: str) -> dict:
#     """Disable a livestream for a specific mint."""
#     return client.request(
#         method="PUT",
#         endpoint=f"/livestreams/{mint}/disable-livestream"
#     )


# def put_livestreams_enable_livestream(mint: str) -> dict:
#     """Enable a livestream for a specific mint."""
#     return client.request(
#         method="PUT",
#         endpoint=f"/livestreams/{mint}/enable-livestream"
#     )


# def put_livestreams_unban_livestream(mint: str) -> dict:
#     """Unban a livestream for a specific mint."""
#     return client.request(
#         method="PUT",
#         endpoint=f"/livestreams/{mint}/unban-livestream"
#     )


# def put_livestreams_ban_livestream(mint: str) -> dict:
#     """Ban a livestream for a specific mint."""
#     return client.request(
#         method="PUT",
#         endpoint=f"/livestreams/{mint}/ban-livestream"
#     )


# def post_livestreams_call_webhook(x_signature: str) -> dict:
#     """Call a webhook for livestreams with the specified x-signature."""
#     return client.request(
#         method="POST",
#         endpoint="/livestreams/call-webhook",
#         headers={
#             "x-signature": x_signature
#         }
#     )


# def post_livestreams_livekit_webhook(authorization: str) -> dict:
#     """Call a LiveKit webhook for livestreams with the specified authorization."""
#     return client.request(
#         method="POST",
#         endpoint="/livestreams/livekit-webhook",
#         headers={
#             "Authorization": authorization
#         }
#     )


# def post_reports() -> dict:
#     """Create a new report."""
#     return client.request(
#         method="POST",
#         endpoint="/reports",
#         json={}
#     )


def get_reports(limit: int, offset: int, report_type: str, done: str, created_at_from: str, created_at_to: str, is_currently_live: str) -> dict:
    """Get reports with specified query parameters."""
    return client.request(
        method="GET",
        endpoint="/reports",
        params={
            "limit": limit,
            "offset": offset,
            "type": report_type,
            "done": done,
            "createdAtFrom": created_at_from,
            "createdAtTo": created_at_to,
            "isCurrentlyLive": is_currently_live
        }
    )


# def post_reports_update() -> dict:
#     """Update a report."""
#     return client.request(
#         method="POST",
#         endpoint="/reports/update",
#         json={}
#     )


# def delete_report(report_id: str) -> dict:
#     """Delete a report by its ID."""
#     return client.request(
#         method="DELETE",
#         endpoint=f"/reports/{report_id}"
#     )


# def post_reports_report_comment(x_client_key: str) -> dict:
#     """Report a comment with the specified client key."""
#     return client.request(
#         method="POST",
#         endpoint="/reports/reportComment",
#         headers={
#             "x-client-key": x_client_key
#         }
#     )


# def post_captcha_score(captcha_token: str) -> dict:
#     """Submit a captcha token and get the score."""
#     return client.request(
#         method="POST",
#         endpoint="/captcha-score",
#         params={
#             "captchaToken": captcha_token
#         }
#     )


def get_pinata_health() -> dict:
    """Check the health of the Pinata service."""
    return client.request(
        method="GET",
        endpoint="/pinata-health/health"
    )


def get_pinata_upload_health() -> dict:
    """Check the upload health of the Pinata service."""
    return client.request(
        method="GET",
        endpoint="/pinata-health/upload-health"
    )


def get_pinata_download_health() -> dict:
    """Check the download health of the Pinata service."""
    return client.request(
        method="GET",
        endpoint="/pinata-health/download-health"
    )


# def post_activity_click() -> dict:
#     """Register a click activity."""
#     return client.request(
#         method="POST",
#         endpoint="/activity/click"
#     )


# def post_activity_convert() -> dict:
#     """Register a convert activity."""
#     return client.request(
#         method="POST",
#         endpoint="/activity/convert"
#     )


# def post_activity_seen() -> dict:
#     """Register a seen activity."""
#     return client.request(
#         method="POST",
#         endpoint="/activity/seen",
#         json={}
#     )


# def post_activity_click_advanced() -> dict:
#     """Register an advanced click activity."""
#     return client.request(
#         method="POST",
#         endpoint="/activity/click-advanced"
#     )


# def post_activity_convert_advanced() -> dict:
#     """Register an advanced convert activity."""
#     return client.request(
#         method="POST",
#         endpoint="/activity/convert-advanced"
#     )


# def post_activity_seen_advanced() -> dict:
#     """Register an advanced seen activity."""
#     return client.request(
#         method="POST",
#         endpoint="/activity/seen-advanced",
#         json={}
#     )


def get_era() -> dict:
    """Get the current era."""
    return client.request(
        method="GET",
        endpoint="/era"
    )


def get_eras() -> dict:
    """Get all eras."""
    return client.request(
        method="GET",
        endpoint="/eras"
    )


def get_meet() -> dict:
    """Get the meet information."""
    return client.request(
        method="GET",
        endpoint="/meet"
    )


# def post_meet_dismiss() -> dict:
#     """Dismiss the meet."""
#     return client.request(
#         method="POST",
#         endpoint="/meet/dismiss"
#     )


# def post_meet_copy_email() -> dict:
#     """Copy the meet email."""
#     return client.request(
#         method="POST",
#         endpoint="/meet/copy-email"
#     )


# def post_meet_join() -> dict:
#     """Join the meet."""
#     return client.request(
#         method="POST",
#         endpoint="/meet/join"
#     )


# def post_meet_reset() -> dict:
#     """Reset the meet."""
#     return client.request(
#         method="POST",
#         endpoint="/meet/reset"
#     )


# def post_meet_create_interviews() -> dict:
#     """Create interviews for the meet."""
#     return client.request(
#         method="POST",
#         endpoint="/meet/create-interviews"
#     )


def get_meet_status(meet_id: str) -> dict:
    """Get the status of a specific meet by meet ID."""
    return client.request(
        method="GET",
        endpoint=f"/meet/{meet_id}/status"
    )


def get_intercom_hmac() -> dict:
    """Get the HMAC for Intercom."""
    return client.request(
        method="GET",
        endpoint="/intercom/hmac"
    )


def get_videos_signed_url(extension: str) -> dict:
    """Get a signed URL for video upload."""
    return client.request(
        method="GET",
        endpoint="/videos/get-signed-url",
        params={
            "extension": extension
        }
    )


def get_videos_previews(filename: str) -> dict:
    """Get previews for a video by filename."""
    return client.request(
        method="GET",
        endpoint="/videos/get-previews",
        params={
            "filename": filename
        }
    )


def get_token_generate_token_for_thread() -> dict:
    """Generate a token for a thread."""
    return client.request(
        method="GET",
        endpoint="/token/generateTokenForThread"
    )


# def post_ipfs_token_metadata() -> dict:
#     """Post token metadata to IPFS."""
#     return client.request(
#         method="POST",
#         endpoint="/ipfs/token-metadata",
#         json={}
#     )


# def post_ipfs_image() -> dict:
#     """Post an image to IPFS."""
#     return client.request(
#         method="POST",
#         endpoint="/ipfs/image",
#         json={}
#     )


# def post_bookmarks() -> dict:
#     """Create a new bookmark."""
#     return client.request(
#         method="POST",
#         endpoint="/bookmarks",
#         json={}
#     )


def get_bookmarks(with_preview_images: bool) -> dict:
    """Get bookmarks with an option to include preview images."""
    return client.request(
        method="GET",
        endpoint="/bookmarks",
        params={
            "withPreviewImages": str(with_preview_images).lower()
        }
    )


def get_bookmarks_default(with_details: bool) -> dict:
    """Get default bookmarks with an option to include details."""
    return client.request(
        method="GET",
        endpoint="/bookmarks/default",
        params={
            "withDetails": str(with_details).lower()
        }
    )


def get_bookmark_by_id(bookmark_id: str, with_details: bool) -> dict:
    """Get a specific bookmark by ID with an option to include details."""
    return client.request(
        method="GET",
        endpoint=f"/bookmarks/{bookmark_id}",
        params={
            "withDetails": str(with_details).lower()
        }
    )


# def put_bookmark_by_id(bookmark_id: str) -> dict:
#     """Update a specific bookmark by ID."""
#     return client.request(
#         method="PUT",
#         endpoint=f"/bookmarks/{bookmark_id}"
#     )


# def delete_bookmark_by_id(bookmark_id: str) -> dict:
#     """Delete a specific bookmark by ID."""
#     return client.request(
#         method="DELETE",
#         endpoint=f"/bookmarks/{bookmark_id}"
#     )


# def post_bookmark_item(data: dict) -> dict:
#     """Add a new bookmark item."""
#     return client.request(
#         method="POST",
#         endpoint="/bookmarks/items/add",
#         json=data
#     )


# def post_bookmark_item_remove(data: dict) -> dict:
#     """Remove a bookmark item."""
#     return client.request(
#         method="POST",
#         endpoint="/bookmarks/items/remove",
#         json=data
#     )


# def post_default_bookmark_item(data: dict) -> dict:
#     """Add a new default bookmark item."""
#     return client.request(
#         method="POST",
#         endpoint="/bookmarks/default/items",
#         json=data
#     )


# def post_bookmark_item_by_id(bookmark_id: str, data: dict) -> dict:
#     """Add a new item to a specific bookmark by ID."""
#     return client.request(
#         method="POST",
#         endpoint=f"/bookmarks/{bookmark_id}/items",
#         json=data
#     )


def get_bookmark_item_by_id(item_id: str, with_users: bool) -> dict:
    """Get a specific bookmark item by ID with an option to include users."""
    return client.request(
        method="GET",
        endpoint=f"/bookmarks/items/{item_id}",
        params={
            "withUsers": str(with_users).lower()
        }
    )


def delete_default_bookmark_item(item_id: str) -> dict:
    """Delete a default bookmark item by ID."""
    return client.request(
        method="DELETE",
        endpoint=f"/bookmarks/default/{item_id}"
    )


def delete_bookmark_item_by_id(bookmark_id: str, item_id: str) -> dict:
    """Delete a specific item from a bookmark by bookmark ID and item ID."""
    return client.request(
        method="DELETE",
        endpoint=f"/bookmarks/{bookmark_id}/{item_id}"
    )


