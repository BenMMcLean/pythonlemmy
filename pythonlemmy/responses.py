from typing import Optional
import requests

from .views import *
from .objects import *


class AddAdminResponse(object):
    admins: list[PersonView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.admins = [PersonView(e) for e in response["admins"]]


class AddModToCommunityResponse(object):
    moderators: list[CommunityModeratorView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.moderators = [CommunityModeratorView(e) for e in response["moderators"]]


class BanFromCommunityResponse(object):
    person_view: PersonView = None
    banned: bool = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.person_view = PersonView(response["person_view"])
        self.banned = response["banned"]


class BanPersonResponse(object):
    person_view: PersonView = None
    banned: bool = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.person_view = PersonView(response["person_view"])
        self.banned = response["banned"]


class BannedPersonsResponse(object):
    banned: list[PersonView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.banned = [PersonView(e) for e in response["banned"]]


class BlockCommunityResponse(object):
    community_view: CommunityView = None
    blocked: bool = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.community_view = CommunityView(response["community_view"])
        self.blocked = response["blocked"]


class BlockInstanceResponse(object):
    blocked: bool = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.blocked = response["blocked"]


class BlockPersonResponse(object):
    person_view: PersonView = None
    blocked: bool = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.person_view = PersonView(response["person_view"])
        self.blocked = response["blocked"]


class CaptchaResponse(object):
    png: str = None
    wav: str = None
    uuid: str = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.png = response["png"]
        self.wav = response["wav"]
        self.uuid = response["uuid"]


class CommentReplyResponse(object):
    comment_reply_view: CommentReplyView = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.comment_reply_view = CommentReplyView(response["comment_reply_view"])


class CommentReportResponse(object):
    comment_report_view: CommentReportView = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.comment_report_view = CommentReportView(response["comment_report_view"])


class CommentResponse(object):
    comment_view: CommentView = None
    recipient_ids: list[int] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.comment_view = CommentView(response["comment_view"])
        self.recipient_ids = [int(e) for e in response["recipient_ids"]]


class CommunityResponse(object):
    community_view: CommunityView = None
    discussion_languages: list[int] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.community_view = CommunityView(response["community_view"])
        self.discussion_languages = [int(e) for e in response["discussion_languages"]]


class CustomEmojiResponse(object):
    custom_emoji: CustomEmojiView = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.custom_emoji = CustomEmojiView(response["custom_emoji"])


class GenerateTotpSecretResponse(object):
    totp_secret_url: str = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.totp_secret_url = response["totp_secret_url"]


class GetCaptchaResponse(object):
    ok: Optional[CaptchaResponse] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.ok = CaptchaResponse(response["ok"])


class GetCommentsResponse(object):
    comments: list[CommentView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.comments = [CommentView(e) for e in response["comments"]]


class GetCommunityResponse(object):
    community_view: CommunityView = None
    site: Optional[Site] = None
    moderators: list[CommunityModeratorView] = None
    discussion_languages: list[int] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.community_view = CommunityView(response["community_view"])
        self.site = Site(response["site"])
        self.moderators = [CommunityModeratorView(e) for e in response["moderators"]]
        self.discussion_languages = [int(e) for e in response["discussion_languages"]]


class GetFederatedInstancesResponse(object):
    federated_instances: Optional[FederatedInstances] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.federated_instances = FederatedInstances(response["federated_instances"])


class GetModlogResponse(object):
    removed_posts: list[ModRemovePostView] = None
    locked_posts: list[ModLockPostView] = None
    featured_posts: list[ModFeaturePostView] = None
    removed_comments: list[ModRemoveCommentView] = None
    removed_communities: list[ModRemoveCommunityView] = None
    banned_from_community: list[ModBanFromCommunityView] = None
    banned: list[ModBanView] = None
    added_to_community: list[ModAddCommunityView] = None
    transferred_to_community: list[ModTransferCommunityView] = None
    added: list[ModAddView] = None
    admin_purged_persons: list[AdminPurgePersonView] = None
    admin_purged_communities: list[AdminPurgeCommunityView] = None
    admin_purged_posts: list[AdminPurgePostView] = None
    admin_purged_comments: list[AdminPurgeCommentView] = None
    hidden_communities: list[ModHideCommunityView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.removed_posts = [ModRemovePostView(e) for e in response["removed_posts"]]
        self.locked_posts = [ModLockPostView(e) for e in response["locked_posts"]]
        self.featured_posts = [ModFeaturePostView(e) for e in response["featured_posts"]]
        self.removed_comments = [ModRemoveCommentView(e) for e in response["removed_comments"]]
        self.removed_communities = [ModRemoveCommunityView(e) for e in response["removed_communities"]]
        self.banned_from_community = [ModBanFromCommunityView(e) for e in response["banned_from_community"]]
        self.banned = [ModBanView(e) for e in response["banned"]]
        self.added_to_community = [ModAddCommunityView(e) for e in response["added_to_community"]]
        self.transferred_to_community = [ModTransferCommunityView(e) for e in response["transferred_to_community"]]
        self.added = [ModAddView(e) for e in response["added"]]
        self.admin_purged_persons = [AdminPurgePersonView(e) for e in response["admin_purged_persons"]]
        self.admin_purged_communities = [AdminPurgeCommunityView(e) for e in response["admin_purged_communities"]]
        self.admin_purged_posts = [AdminPurgePostView(e) for e in response["admin_purged_posts"]]
        self.admin_purged_comments = [AdminPurgeCommentView(e) for e in response["admin_purged_comments"]]
        self.hidden_communities = [ModHideCommunityView(e) for e in response["hidden_communities"]]


class GetPersonDetailsResponse(object):
    person_view: PersonView = None
    site: Optional[Site] = None
    comments: list[CommentView] = None
    posts: list[PostView] = None
    moderates: list[CommunityModeratorView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.person_view = PersonView(response["person_view"])
        self.site = Site(response["site"])
        self.comments = [CommentView(e) for e in response["comments"]]
        self.posts = [PostView(e) for e in response["posts"]]
        self.moderates = [CommunityModeratorView(e) for e in response["moderates"]]


class GetPersonMentionsResponse(object):
    mentions: list[PersonMentionView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.mentions = [PersonMentionView(e) for e in response["mentions"]]


class GetPostResponse(object):
    post_view: PostView = None
    community_view: CommunityView = None
    moderators: list[CommunityModeratorView] = None
    cross_posts: list[PostView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.post_view = PostView(response["post_view"])
        self.community_view = CommunityView(response["community_view"])
        self.moderators = [CommunityModeratorView(e) for e in response["moderators"]]
        self.cross_posts = [PostView(e) for e in response["cross_posts"]]


class GetPostsResponse(object):
    posts: list[PostView] = None
    next_page: Optional[str] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.posts = [PostView(e) for e in response["posts"]]
        self.next_page = response["next_page"]


class GetRepliesResponse(object):
    replies: list[CommentReplyView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.replies = [CommentReplyView(e) for e in response["replies"]]


class GetReportCountResponse(object):
    community_id: Optional[int] = None
    comment_reports: int = None
    post_reports: int = None
    private_message_reports: Optional[int] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.community_id = response["community_id"]
        self.comment_reports = response["comment_reports"]
        self.post_reports = response["post_reports"]
        self.private_message_reports = response["private_message_reports"]


class GetSiteMetadataResponse(object):
    metadata: LinkMetadata = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.metadata = LinkMetadata(response["metadata"])


class GetSiteResponse(object):
    site_view: SiteView = None
    admins: list[PersonView] = None
    version: str = None
    my_user: Optional[MyUserInfo] = None
    all_languages: list[Language] = None
    discussion_languages: list[int] = None
    taglines: list[Tagline] = None
    custom_emojis: list[CustomEmojiView] = None
    blocked_urls: list[LocalSiteUrlBlocklist] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.site_view = SiteView(response["site_view"])
        self.admins = [PersonView(e) for e in response["admins"]]
        self.version = response["version"]
        self.my_user = MyUserInfo(response["my_user"])
        self.all_languages = [Language(e) for e in response["all_languages"]]
        self.discussion_languages = [int(e) for e in response["discussion_languages"]]
        self.taglines = [Tagline(e) for e in response["taglines"]]
        self.custom_emojis = [CustomEmojiView(e) for e in response["custom_emojis"]]
        self.blocked_urls = [LocalSiteUrlBlocklist(e) for e in response["blocked_urls"]]


class GetUnreadCountResponse(object):
    replies: int = None
    mentions: int = None
    private_messages: int = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.replies = response["replies"]
        self.mentions = response["mentions"]
        self.private_messages = response["private_messages"]


class GetUnreadRegistrationApplicationCountResponse(object):
    registration_applications: int = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.registration_applications = response["registration_applications"]


class ListCommentLikesResponse(object):
    comment_likes: list[VoteView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.comment_likes = [VoteView(e) for e in response["comment_likes"]]


class ListCommentReportsResponse(object):
    comment_reports: list[CommentReportView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.comment_reports = [CommentReportView(e) for e in response["comment_reports"]]


class ListCommunitiesResponse(object):
    communities: list[CommunityView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.communities = [CommunityView(e) for e in response["communities"]]


class ListMediaResponse(object):
    images: list[LocalImageView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.images = [LocalImageView(e) for e in response["images"]]


class ListPostLikesResponse(object):
    post_likes: list[VoteView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.post_likes = [VoteView(e) for e in response["post_likes"]]


class ListPostReportsResponse(object):
    post_reports: list[PostReportView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.post_reports = [PostReportView(e) for e in response["post_reports"]]


class ListPrivateMessageReportsResponse(object):
    private_message_reports: list[PrivateMessageReportView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.private_message_reports = [PrivateMessageReportView(e) for e in response["private_message_reports"]]


class ListRegistrationApplicationsResponse(object):
    registration_applications: list[RegistrationApplicationView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.registration_applications = [RegistrationApplicationView(e) for e in response["registration_applications"]]


class LoginResponse(object):
    jwt: Optional[str] = None
    registration_created: bool = None
    verify_email_sent: bool = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.jwt = response["jwt"]
        self.registration_created = response["registration_created"]
        self.verify_email_sent = response["verify_email_sent"]


class PersonMentionResponse(object):
    person_mention_view: PersonMentionView = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.person_mention_view = PersonMentionView(response["person_mention_view"])


class PostReportResponse(object):
    post_report_view: PostReportView = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.post_report_view = PostReportView(response["post_report_view"])


class PostResponse(object):
    post_view: PostView = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.post_view = PostView(response["post_view"])


class PrivateMessageReportResponse(object):
    private_message_report_view: PrivateMessageReportView = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.private_message_report_view = PrivateMessageReportView(response["private_message_report_view"])


class PrivateMessageResponse(object):
    private_message_view: PrivateMessageView = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.private_message_view = PrivateMessageView(response["private_message_view"])


class PrivateMessagesResponse(object):
    private_messages: list[PrivateMessageView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.private_messages = [PrivateMessageView(e) for e in response["private_messages"]]


class RegistrationApplicationResponse(object):
    registration_application: RegistrationApplicationView = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.registration_application = RegistrationApplicationView(response["registration_application"])


class ResolveObjectResponse(object):
    comment: Optional[CommentView] = None
    post: Optional[PostView] = None
    community: Optional[CommunityView] = None
    person: Optional[PersonView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.comment = CommentView(response["comment"])
        self.post = PostView(response["post"])
        self.community = CommunityView(response["community"])
        self.person = PersonView(response["person"])


class SearchResponse(object):
    type_: str = None
    comments: list[CommentView] = None
    posts: list[PostView] = None
    communities: list[CommunityView] = None
    users: list[PersonView] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.type_ = response["type_"]
        self.comments = [CommentView(e) for e in response["comments"]]
        self.posts = [PostView(e) for e in response["posts"]]
        self.communities = [CommunityView(e) for e in response["communities"]]
        self.users = [PersonView(e) for e in response["users"]]


class SiteResponse(object):
    site_view: SiteView = None
    taglines: list[Tagline] = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.site_view = SiteView(response["site_view"])
        self.taglines = [Tagline(e) for e in response["taglines"]]


class SuccessResponse(object):
    success: bool = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.success = response["success"]


class UpdateTotpResponse(object):
    enabled: bool = None

    def __init__(self, api_response: requests.Response) -> None:
        response = api_response.json()
        self.enabled = response["enabled"]
