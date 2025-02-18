from .client import client


def hello_world() -> str:
    """Return a greeting."""
    return client.request(
        method="GET",
        endpoint="/"
    )


def health_check() -> dict:
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


