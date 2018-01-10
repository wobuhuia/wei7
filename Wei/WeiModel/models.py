# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CaptchaCaptchastore(models.Model):
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ImsAccount(models.Model):
    acid = models.AutoField(primary_key=True)
    uniacid = models.PositiveIntegerField()
    hash = models.CharField(max_length=8)
    type = models.PositiveIntegerField()
    isconnect = models.IntegerField()
    isdeleted = models.PositiveIntegerField()
    endtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_account'


class ImsAccountWebapp(models.Model):
    acid = models.IntegerField(primary_key=True)
    uniacid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ims_account_webapp'


class ImsAccountWechats(models.Model):
    acid = models.PositiveIntegerField(primary_key=True)
    uniacid = models.PositiveIntegerField()
    token = models.CharField(max_length=32)
    encodingaeskey = models.CharField(max_length=255)
    level = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    account = models.CharField(max_length=30)
    original = models.CharField(max_length=50)
    signature = models.CharField(max_length=100)
    country = models.CharField(max_length=10)
    province = models.CharField(max_length=3)
    city = models.CharField(max_length=15)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    lastupdate = models.PositiveIntegerField()
    key = models.CharField(max_length=50)
    secret = models.CharField(max_length=50)
    styleid = models.PositiveIntegerField()
    subscribeurl = models.CharField(max_length=120)
    auth_refresh_token = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_account_wechats'


class ImsAccountWxapp(models.Model):
    acid = models.AutoField(primary_key=True)
    uniacid = models.IntegerField()
    token = models.CharField(max_length=32)
    encodingaeskey = models.CharField(max_length=43)
    level = models.IntegerField()
    account = models.CharField(max_length=30)
    original = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    secret = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    appdomain = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_account_wxapp'


class ImsArticleCategory(models.Model):
    title = models.CharField(max_length=30)
    displayorder = models.PositiveIntegerField()
    type = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'ims_article_category'


class ImsArticleNews(models.Model):
    cateid = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumb = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    displayorder = models.PositiveIntegerField()
    is_display = models.PositiveIntegerField()
    is_show_home = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()
    click = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_article_news'


class ImsArticleNotice(models.Model):
    cateid = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    displayorder = models.PositiveIntegerField()
    is_display = models.PositiveIntegerField()
    is_show_home = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()
    click = models.PositiveIntegerField()
    style = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ims_article_notice'


class ImsArticleUnreadNotice(models.Model):
    notice_id = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    is_new = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_article_unread_notice'


class ImsBasicReply(models.Model):
    rid = models.PositiveIntegerField()
    content = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'ims_basic_reply'


class ImsBusiness(models.Model):
    weid = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    thumb = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    phone = models.CharField(max_length=15)
    qq = models.CharField(max_length=15)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    dist = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    lng = models.CharField(max_length=10)
    lat = models.CharField(max_length=10)
    industry1 = models.CharField(max_length=10)
    industry2 = models.CharField(max_length=10)
    createtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_business'


class ImsCoreAttachment(models.Model):
    uniacid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    filename = models.CharField(max_length=255)
    attachment = models.CharField(max_length=255)
    type = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()
    module_upload_dir = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ims_core_attachment'


class ImsCoreCache(models.Model):
    key = models.CharField(primary_key=True, max_length=50)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'ims_core_cache'


class ImsCoreCron(models.Model):
    cloudid = models.PositiveIntegerField()
    module = models.CharField(max_length=50)
    uniacid = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)
    lastruntime = models.PositiveIntegerField()
    nextruntime = models.PositiveIntegerField()
    weekday = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.CharField(max_length=255)
    extra = models.CharField(max_length=5000)
    status = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_core_cron'


class ImsCoreCronRecord(models.Model):
    uniacid = models.PositiveIntegerField()
    module = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    tid = models.PositiveIntegerField()
    note = models.CharField(max_length=500)
    tag = models.CharField(max_length=5000)
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_core_cron_record'


class ImsCoreMenu(models.Model):
    pid = models.PositiveIntegerField()
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=255)
    append_title = models.CharField(max_length=30)
    append_url = models.CharField(max_length=255)
    displayorder = models.PositiveIntegerField()
    type = models.CharField(max_length=15)
    is_display = models.PositiveIntegerField()
    is_system = models.PositiveIntegerField()
    permission_name = models.CharField(max_length=50)
    group_name = models.CharField(max_length=30)
    icon = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ims_core_menu'


class ImsCorePaylog(models.Model):
    plid = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    uniacid = models.IntegerField()
    acid = models.IntegerField()
    openid = models.CharField(max_length=40)
    uniontid = models.CharField(max_length=64)
    tid = models.CharField(max_length=128)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField()
    module = models.CharField(max_length=50)
    tag = models.CharField(max_length=2000)
    is_usecard = models.PositiveIntegerField()
    card_type = models.PositiveIntegerField()
    card_id = models.CharField(max_length=50)
    card_fee = models.DecimalField(max_digits=10, decimal_places=2)
    encrypt_code = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ims_core_paylog'


class ImsCorePerformance(models.Model):
    type = models.IntegerField()
    runtime = models.CharField(max_length=10)
    runurl = models.CharField(max_length=512)
    runsql = models.CharField(max_length=512)
    createtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_core_performance'


class ImsCoreQueue(models.Model):
    qid = models.BigAutoField(primary_key=True)
    uniacid = models.PositiveIntegerField()
    acid = models.PositiveIntegerField()
    message = models.CharField(max_length=2000)
    params = models.CharField(max_length=1000)
    keyword = models.CharField(max_length=1000)
    response = models.CharField(max_length=2000)
    module = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_core_queue'


class ImsCoreRefundlog(models.Model):
    uniacid = models.IntegerField()
    refund_uniontid = models.CharField(max_length=64)
    reason = models.CharField(max_length=80)
    uniontid = models.CharField(max_length=64)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_core_refundlog'


class ImsCoreResource(models.Model):
    mid = models.AutoField(primary_key=True)
    uniacid = models.PositiveIntegerField()
    media_id = models.CharField(max_length=100)
    trunk = models.PositiveIntegerField()
    type = models.CharField(max_length=10)
    dateline = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_core_resource'


class ImsCoreSendsmsLog(models.Model):
    uniacid = models.PositiveIntegerField()
    mobile = models.CharField(max_length=11)
    content = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_core_sendsms_log'


class ImsCoreSessions(models.Model):
    sid = models.CharField(primary_key=True, max_length=32)
    uniacid = models.PositiveIntegerField()
    openid = models.CharField(max_length=50)
    data = models.CharField(max_length=5000)
    expiretime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_core_sessions'


class ImsCoreSettings(models.Model):
    key = models.CharField(primary_key=True, max_length=200)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'ims_core_settings'


class ImsCouponLocation(models.Model):
    uniacid = models.PositiveIntegerField()
    acid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    location_id = models.PositiveIntegerField()
    business_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    category = models.CharField(max_length=255)
    province = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    district = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    longitude = models.CharField(max_length=15)
    latitude = models.CharField(max_length=15)
    telephone = models.CharField(max_length=20)
    photo_list = models.CharField(max_length=10000)
    avg_price = models.PositiveIntegerField()
    open_time = models.CharField(max_length=50)
    recommend = models.CharField(max_length=255)
    special = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    offset_type = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    message = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_coupon_location'


class ImsCoverReply(models.Model):
    uniacid = models.PositiveIntegerField()
    multiid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    module = models.CharField(max_length=30)
    do = models.CharField(max_length=30)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    thumb = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_cover_reply'


class ImsCustomReply(models.Model):
    rid = models.PositiveIntegerField()
    start1 = models.IntegerField()
    end1 = models.IntegerField()
    start2 = models.IntegerField()
    end2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_custom_reply'


class ImsImagesReply(models.Model):
    rid = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    mediaid = models.CharField(max_length=255)
    createtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_images_reply'


class ImsMcCashRecord(models.Model):
    uniacid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    clerk_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    clerk_type = models.PositiveIntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    final_fee = models.DecimalField(max_digits=10, decimal_places=2)
    credit1 = models.PositiveIntegerField()
    credit1_fee = models.DecimalField(max_digits=10, decimal_places=2)
    credit2 = models.DecimalField(max_digits=10, decimal_places=2)
    cash = models.DecimalField(max_digits=10, decimal_places=2)
    return_cash = models.DecimalField(max_digits=10, decimal_places=2)
    final_cash = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.CharField(max_length=255)
    createtime = models.PositiveIntegerField()
    trade_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ims_mc_cash_record'


class ImsMcChatsRecord(models.Model):
    uniacid = models.PositiveIntegerField()
    acid = models.PositiveIntegerField()
    flag = models.PositiveIntegerField()
    openid = models.CharField(max_length=32)
    msgtype = models.CharField(max_length=15)
    content = models.CharField(max_length=10000)
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_mc_chats_record'


class ImsMcCreditsRecharge(models.Model):
    uniacid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    openid = models.CharField(max_length=50)
    tid = models.CharField(max_length=64)
    transid = models.CharField(max_length=30)
    fee = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
    tag = models.CharField(max_length=10)
    status = models.IntegerField()
    createtime = models.PositiveIntegerField()
    backtype = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_mc_credits_recharge'


class ImsMcCreditsRecord(models.Model):
    uid = models.PositiveIntegerField()
    uniacid = models.IntegerField()
    credittype = models.CharField(max_length=10)
    num = models.DecimalField(max_digits=10, decimal_places=2)
    operator = models.PositiveIntegerField()
    module = models.CharField(max_length=30)
    clerk_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    clerk_type = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()
    remark = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ims_mc_credits_record'


class ImsMcFansGroups(models.Model):
    uniacid = models.PositiveIntegerField()
    acid = models.PositiveIntegerField()
    groups = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'ims_mc_fans_groups'


class ImsMcFansTagMapping(models.Model):
    fanid = models.PositiveIntegerField()
    tagid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_mc_fans_tag_mapping'
        unique_together = (('fanid', 'tagid'),)


class ImsMcGroups(models.Model):
    groupid = models.AutoField(primary_key=True)
    uniacid = models.IntegerField()
    title = models.CharField(max_length=20)
    credit = models.PositiveIntegerField()
    isdefault = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_mc_groups'


class ImsMcHandsel(models.Model):
    uniacid = models.IntegerField()
    touid = models.PositiveIntegerField()
    fromuid = models.CharField(max_length=32)
    module = models.CharField(max_length=30)
    sign = models.CharField(max_length=100)
    action = models.CharField(max_length=20)
    credit_value = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_mc_handsel'


class ImsMcMappingFans(models.Model):
    fanid = models.AutoField(primary_key=True)
    acid = models.PositiveIntegerField()
    uniacid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    openid = models.CharField(unique=True, max_length=50)
    nickname = models.CharField(max_length=50)
    groupid = models.CharField(max_length=30)
    salt = models.CharField(max_length=8)
    follow = models.PositiveIntegerField()
    followtime = models.PositiveIntegerField()
    unfollowtime = models.PositiveIntegerField()
    tag = models.CharField(max_length=1000)
    updatetime = models.PositiveIntegerField(blank=True, null=True)
    unionid = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'ims_mc_mapping_fans'


class ImsMcMappingUcenter(models.Model):
    uniacid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    centeruid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_mc_mapping_ucenter'


class ImsMcMassRecord(models.Model):
    uniacid = models.PositiveIntegerField()
    acid = models.PositiveIntegerField()
    groupname = models.CharField(max_length=50)
    fansnum = models.PositiveIntegerField()
    msgtype = models.CharField(max_length=10)
    content = models.CharField(max_length=10000)
    group = models.IntegerField()
    attach_id = models.PositiveIntegerField()
    media_id = models.CharField(max_length=100)
    type = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    cron_id = models.PositiveIntegerField()
    sendtime = models.PositiveIntegerField()
    finalsendtime = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_mc_mass_record'


class ImsMcMemberAddress(models.Model):
    uniacid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    username = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    zipcode = models.CharField(max_length=6)
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    district = models.CharField(max_length=32)
    address = models.CharField(max_length=512)
    isdefault = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_mc_member_address'


class ImsMcMemberFields(models.Model):
    uniacid = models.IntegerField()
    fieldid = models.IntegerField()
    title = models.CharField(max_length=255)
    available = models.IntegerField()
    displayorder = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_mc_member_fields'


class ImsMcMemberProperty(models.Model):
    uniacid = models.IntegerField()
    property = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ims_mc_member_property'


class ImsMcMembers(models.Model):
    uid = models.AutoField(primary_key=True)
    uniacid = models.PositiveIntegerField()
    mobile = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    salt = models.CharField(max_length=8)
    groupid = models.IntegerField()
    credit1 = models.DecimalField(max_digits=10, decimal_places=2)
    credit2 = models.DecimalField(max_digits=10, decimal_places=2)
    credit3 = models.DecimalField(max_digits=10, decimal_places=2)
    credit4 = models.DecimalField(max_digits=10, decimal_places=2)
    credit5 = models.DecimalField(max_digits=10, decimal_places=2)
    credit6 = models.DecimalField(max_digits=10, decimal_places=2)
    createtime = models.PositiveIntegerField()
    realname = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)
    avatar = models.CharField(max_length=255)
    qq = models.CharField(max_length=15)
    vip = models.PositiveIntegerField()
    gender = models.IntegerField()
    birthyear = models.PositiveSmallIntegerField()
    birthmonth = models.PositiveIntegerField()
    birthday = models.PositiveIntegerField()
    constellation = models.CharField(max_length=10)
    zodiac = models.CharField(max_length=5)
    telephone = models.CharField(max_length=15)
    idcard = models.CharField(max_length=30)
    studentid = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    nationality = models.CharField(max_length=30)
    resideprovince = models.CharField(max_length=30)
    residecity = models.CharField(max_length=30)
    residedist = models.CharField(max_length=30)
    graduateschool = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    education = models.CharField(max_length=10)
    occupation = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    revenue = models.CharField(max_length=10)
    affectivestatus = models.CharField(max_length=30)
    lookingfor = models.CharField(max_length=255)
    bloodtype = models.CharField(max_length=5)
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    alipay = models.CharField(max_length=30)
    msn = models.CharField(max_length=30)
    taobao = models.CharField(max_length=30)
    site = models.CharField(max_length=30)
    bio = models.TextField()
    interest = models.TextField()

    class Meta:
        managed = False
        db_table = 'ims_mc_members'


class ImsMcOauthFans(models.Model):
    oauth_openid = models.CharField(max_length=50)
    acid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    openid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ims_mc_oauth_fans'


class ImsMenuEvent(models.Model):
    uniacid = models.PositiveIntegerField()
    keyword = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    picmd5 = models.CharField(max_length=32)
    openid = models.CharField(max_length=128)
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_menu_event'


class ImsMessageNoticeLog(models.Model):
    message = models.CharField(max_length=255)
    is_read = models.IntegerField()
    uid = models.IntegerField()
    sign = models.CharField(max_length=22)
    type = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField()
    end_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_message_notice_log'


class ImsMobilenumber(models.Model):
    rid = models.IntegerField()
    enabled = models.PositiveIntegerField()
    dateline = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ims_mobilenumber'


class ImsModules(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    version = models.CharField(max_length=15)
    ability = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    author = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    settings = models.IntegerField()
    subscribes = models.CharField(max_length=500)
    handles = models.CharField(max_length=500)
    isrulefields = models.IntegerField()
    issystem = models.PositiveIntegerField()
    target = models.PositiveIntegerField()
    iscard = models.PositiveIntegerField()
    permissions = models.CharField(max_length=5000)
    title_initial = models.CharField(max_length=1)
    wxapp_support = models.IntegerField()
    app_support = models.IntegerField()
    welcome_support = models.IntegerField()
    oauth_type = models.IntegerField()
    webapp_support = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_modules'


class ImsModulesBindings(models.Model):
    eid = models.AutoField(primary_key=True)
    module = models.CharField(max_length=100)
    entry = models.CharField(max_length=10)
    call = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    do = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    direct = models.IntegerField()
    url = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    displayorder = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_modules_bindings'


class ImsModulesPlugin(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    main_module = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ims_modules_plugin'


class ImsModulesRank(models.Model):
    module_name = models.CharField(max_length=100)
    uid = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_modules_rank'


class ImsModulesRecycle(models.Model):
    modulename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_modules_recycle'


class ImsMusicReply(models.Model):
    rid = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=300)
    hqurl = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'ims_music_reply'


class ImsNewsReply(models.Model):
    rid = models.PositiveIntegerField()
    parent_id = models.IntegerField()
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    thumb = models.CharField(max_length=500)
    content = models.TextField()
    url = models.CharField(max_length=255)
    displayorder = models.IntegerField()
    incontent = models.IntegerField()
    createtime = models.IntegerField()
    media_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ims_news_reply'


class ImsProfileFields(models.Model):
    field = models.CharField(max_length=255)
    available = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    displayorder = models.SmallIntegerField()
    required = models.IntegerField()
    unchangeable = models.IntegerField()
    showinregister = models.IntegerField()
    field_length = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_profile_fields'


class ImsQrcode(models.Model):
    uniacid = models.PositiveIntegerField()
    acid = models.PositiveIntegerField()
    type = models.CharField(max_length=10)
    extra = models.PositiveIntegerField()
    qrcid = models.BigIntegerField()
    scene_str = models.CharField(max_length=64)
    name = models.CharField(max_length=50)
    keyword = models.CharField(max_length=100)
    model = models.PositiveIntegerField()
    ticket = models.CharField(max_length=250)
    url = models.CharField(max_length=256)
    expire = models.PositiveIntegerField()
    subnum = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_qrcode'


class ImsQrcodeStat(models.Model):
    uniacid = models.PositiveIntegerField()
    acid = models.PositiveIntegerField()
    qid = models.PositiveIntegerField()
    openid = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    qrcid = models.BigIntegerField()
    scene_str = models.CharField(max_length=64)
    name = models.CharField(max_length=50)
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_qrcode_stat'


class ImsRule(models.Model):
    uniacid = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    module = models.CharField(max_length=50)
    displayorder = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    containtype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ims_rule'


class ImsRuleKeyword(models.Model):
    rid = models.PositiveIntegerField()
    uniacid = models.PositiveIntegerField()
    module = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    type = models.PositiveIntegerField()
    displayorder = models.PositiveIntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_rule_keyword'


class ImsSiteArticle(models.Model):
    uniacid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    kid = models.PositiveIntegerField()
    iscommend = models.IntegerField()
    ishot = models.PositiveIntegerField()
    pcate = models.PositiveIntegerField()
    ccate = models.PositiveIntegerField()
    template = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    content = models.TextField()
    thumb = models.CharField(max_length=255)
    incontent = models.IntegerField()
    source = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    displayorder = models.PositiveIntegerField()
    linkurl = models.CharField(max_length=500)
    createtime = models.PositiveIntegerField()
    edittime = models.IntegerField()
    click = models.PositiveIntegerField()
    type = models.CharField(max_length=10)
    credit = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_site_article'


class ImsSiteCategory(models.Model):
    uniacid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    parentid = models.PositiveIntegerField()
    displayorder = models.PositiveIntegerField()
    enabled = models.PositiveIntegerField()
    icon = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    styleid = models.PositiveIntegerField()
    linkurl = models.CharField(max_length=500)
    ishomepage = models.IntegerField()
    icontype = models.PositiveIntegerField()
    css = models.CharField(max_length=500)
    multiid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_site_category'


class ImsSiteMulti(models.Model):
    uniacid = models.PositiveIntegerField()
    title = models.CharField(max_length=30)
    styleid = models.PositiveIntegerField()
    site_info = models.TextField()
    status = models.PositiveIntegerField()
    bindhost = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_site_multi'


class ImsSiteNav(models.Model):
    uniacid = models.PositiveIntegerField()
    multiid = models.PositiveIntegerField()
    section = models.IntegerField()
    module = models.CharField(max_length=50)
    displayorder = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    position = models.IntegerField()
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=500)
    css = models.CharField(max_length=1000)
    status = models.PositiveIntegerField()
    categoryid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_site_nav'


class ImsSitePage(models.Model):
    uniacid = models.PositiveIntegerField()
    multiid = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    params = models.TextField()
    html = models.TextField()
    multipage = models.TextField()
    type = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()
    goodnum = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_site_page'


class ImsSiteSlide(models.Model):
    uniacid = models.PositiveIntegerField()
    multiid = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    thumb = models.CharField(max_length=255)
    displayorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_site_slide'


class ImsSiteStoreCreateAccount(models.Model):
    uid = models.IntegerField()
    uniacid = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_site_store_create_account'


class ImsSiteStoreGoods(models.Model):
    type = models.IntegerField()
    title = models.CharField(max_length=100)
    module = models.CharField(max_length=50)
    account_num = models.IntegerField()
    wxapp_num = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=15)
    slide = models.CharField(max_length=1000)
    category_id = models.IntegerField()
    title_initial = models.CharField(max_length=1)
    status = models.IntegerField()
    createtime = models.IntegerField()
    synopsis = models.CharField(max_length=255)
    description = models.TextField()
    module_group = models.IntegerField()
    api_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_site_store_goods'


class ImsSiteStoreOrder(models.Model):
    orderid = models.CharField(max_length=28)
    goodsid = models.IntegerField()
    duration = models.IntegerField()
    buyer = models.CharField(max_length=50)
    buyerid = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField()
    changeprice = models.IntegerField()
    createtime = models.IntegerField()
    uniacid = models.IntegerField()
    endtime = models.IntegerField()
    wxapp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_site_store_order'


class ImsSiteStyles(models.Model):
    uniacid = models.PositiveIntegerField()
    templateid = models.PositiveIntegerField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ims_site_styles'


class ImsSiteStylesVars(models.Model):
    uniacid = models.PositiveIntegerField()
    templateid = models.PositiveIntegerField()
    styleid = models.PositiveIntegerField()
    variable = models.CharField(max_length=50)
    content = models.TextField()
    description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ims_site_styles_vars'


class ImsSiteTemplates(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    version = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    sections = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_site_templates'


class ImsStatFans(models.Model):
    uniacid = models.PositiveIntegerField()
    new = models.PositiveIntegerField()
    cancel = models.PositiveIntegerField()
    cumulate = models.IntegerField()
    date = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'ims_stat_fans'


class ImsStatKeyword(models.Model):
    uniacid = models.PositiveIntegerField()
    rid = models.CharField(max_length=10)
    kid = models.PositiveIntegerField()
    hit = models.PositiveIntegerField()
    lastupdate = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_stat_keyword'


class ImsStatMsgHistory(models.Model):
    uniacid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    kid = models.PositiveIntegerField()
    from_user = models.CharField(max_length=50)
    module = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    type = models.CharField(max_length=10)
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_stat_msg_history'


class ImsStatRule(models.Model):
    uniacid = models.PositiveIntegerField()
    rid = models.PositiveIntegerField()
    hit = models.PositiveIntegerField()
    lastupdate = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_stat_rule'


class ImsStatVisit(models.Model):
    uniacid = models.IntegerField()
    module = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    date = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_stat_visit'


class ImsUniAccount(models.Model):
    uniacid = models.AutoField(primary_key=True)
    groupid = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    default_acid = models.PositiveIntegerField()
    rank = models.IntegerField(blank=True, null=True)
    title_initial = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ims_uni_account'


class ImsUniAccountGroup(models.Model):
    uniacid = models.PositiveIntegerField()
    groupid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_uni_account_group'


class ImsUniAccountMenus(models.Model):
    uniacid = models.PositiveIntegerField()
    menuid = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    title = models.CharField(max_length=30)
    sex = models.PositiveIntegerField()
    group_id = models.IntegerField()
    client_platform_type = models.PositiveIntegerField()
    area = models.CharField(max_length=50)
    data = models.TextField()
    status = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()
    isdeleted = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_uni_account_menus'


class ImsUniAccountModules(models.Model):
    uniacid = models.PositiveIntegerField()
    module = models.CharField(max_length=50)
    enabled = models.PositiveIntegerField()
    settings = models.TextField()
    shortcut = models.PositiveIntegerField()
    displayorder = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_uni_account_modules'


class ImsUniAccountUsers(models.Model):
    uniacid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    role = models.CharField(max_length=255)
    rank = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_uni_account_users'


class ImsUniGroup(models.Model):
    owner_uid = models.IntegerField()
    name = models.CharField(max_length=50)
    modules = models.CharField(max_length=15000)
    templates = models.CharField(max_length=5000)
    uniacid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_uni_group'


class ImsUniSettings(models.Model):
    uniacid = models.PositiveIntegerField(primary_key=True)
    passport = models.CharField(max_length=200)
    oauth = models.CharField(max_length=100)
    jsauth_acid = models.PositiveIntegerField()
    uc = models.CharField(max_length=500)
    notify = models.CharField(max_length=2000)
    creditnames = models.CharField(max_length=500)
    creditbehaviors = models.CharField(max_length=500)
    welcome = models.CharField(max_length=60)
    default = models.CharField(max_length=60)
    default_message = models.CharField(max_length=2000)
    payment = models.TextField()
    stat = models.CharField(max_length=300)
    default_site = models.PositiveIntegerField(blank=True, null=True)
    sync = models.PositiveIntegerField()
    recharge = models.CharField(max_length=500)
    tplnotice = models.CharField(max_length=1000)
    grouplevel = models.PositiveIntegerField()
    mcplugin = models.CharField(max_length=500)
    exchange_enable = models.PositiveIntegerField()
    coupon_type = models.PositiveIntegerField()
    menuset = models.TextField()
    statistics = models.CharField(max_length=100)
    bind_domain = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ims_uni_settings'


class ImsUniVerifycode(models.Model):
    uniacid = models.PositiveIntegerField()
    receiver = models.CharField(max_length=50)
    verifycode = models.CharField(max_length=6)
    total = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_uni_verifycode'


class ImsUserapiCache(models.Model):
    key = models.CharField(max_length=32)
    content = models.TextField()
    lastupdate = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_userapi_cache'


class ImsUserapiReply(models.Model):
    rid = models.PositiveIntegerField()
    description = models.CharField(max_length=300)
    apiurl = models.CharField(max_length=300)
    token = models.CharField(max_length=32)
    default_text = models.CharField(max_length=100)
    cachetime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_userapi_reply'


class ImsUsers(models.Model):
    uid = models.AutoField(primary_key=True)
    owner_uid = models.IntegerField()
    groupid = models.PositiveIntegerField()
    founder_groupid = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=200)
    salt = models.CharField(max_length=10)
    type = models.PositiveIntegerField()
    status = models.IntegerField()
    joindate = models.PositiveIntegerField()
    joinip = models.CharField(max_length=15)
    lastvisit = models.PositiveIntegerField()
    lastip = models.CharField(max_length=15)
    remark = models.CharField(max_length=500)
    starttime = models.PositiveIntegerField()
    endtime = models.PositiveIntegerField()
    register_type = models.IntegerField()
    openid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ims_users'


class ImsUsersBind(models.Model):
    uid = models.IntegerField()
    bind_sign = models.CharField(max_length=50)
    third_type = models.IntegerField()
    third_nickname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_users_bind'


class ImsUsersFailedLogin(models.Model):
    ip = models.CharField(max_length=15)
    username = models.CharField(max_length=32)
    count = models.PositiveIntegerField()
    lastupdate = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_users_failed_login'


class ImsUsersFounderGroup(models.Model):
    name = models.CharField(max_length=50)
    package = models.CharField(max_length=5000)
    maxaccount = models.PositiveIntegerField()
    maxsubaccount = models.PositiveIntegerField()
    timelimit = models.PositiveIntegerField()
    maxwxapp = models.PositiveIntegerField()
    maxwebapp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_users_founder_group'


class ImsUsersGroup(models.Model):
    owner_uid = models.IntegerField()
    name = models.CharField(max_length=50)
    package = models.CharField(max_length=5000)
    maxaccount = models.PositiveIntegerField()
    maxsubaccount = models.PositiveIntegerField()
    timelimit = models.PositiveIntegerField()
    maxwxapp = models.PositiveIntegerField()
    maxwebapp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_users_group'


class ImsUsersInvitation(models.Model):
    code = models.CharField(unique=True, max_length=64)
    fromuid = models.PositiveIntegerField()
    inviteuid = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ims_users_invitation'


class ImsUsersPermission(models.Model):
    uniacid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    type = models.CharField(max_length=100)
    permission = models.CharField(max_length=10000)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_users_permission'


class ImsUsersProfile(models.Model):
    uid = models.PositiveIntegerField()
    createtime = models.PositiveIntegerField()
    edittime = models.IntegerField()
    realname = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)
    avatar = models.CharField(max_length=255)
    qq = models.CharField(max_length=15)
    mobile = models.CharField(max_length=11)
    fakeid = models.CharField(max_length=30)
    vip = models.PositiveIntegerField()
    gender = models.IntegerField()
    birthyear = models.PositiveSmallIntegerField()
    birthmonth = models.PositiveIntegerField()
    birthday = models.PositiveIntegerField()
    constellation = models.CharField(max_length=10)
    zodiac = models.CharField(max_length=5)
    telephone = models.CharField(max_length=15)
    idcard = models.CharField(max_length=30)
    studentid = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    nationality = models.CharField(max_length=30)
    resideprovince = models.CharField(max_length=30)
    residecity = models.CharField(max_length=30)
    residedist = models.CharField(max_length=30)
    graduateschool = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    education = models.CharField(max_length=10)
    occupation = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    revenue = models.CharField(max_length=10)
    affectivestatus = models.CharField(max_length=30)
    lookingfor = models.CharField(max_length=255)
    bloodtype = models.CharField(max_length=5)
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    alipay = models.CharField(max_length=30)
    msn = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    taobao = models.CharField(max_length=30)
    site = models.CharField(max_length=30)
    bio = models.TextField()
    interest = models.TextField()
    workerid = models.CharField(max_length=64)
    is_send_mobile_status = models.IntegerField()
    send_expire_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_users_profile'


class ImsVideoReply(models.Model):
    rid = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    mediaid = models.CharField(max_length=255)
    createtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_video_reply'


class ImsVoiceReply(models.Model):
    rid = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    mediaid = models.CharField(max_length=255)
    createtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_voice_reply'


class ImsWechatAttachment(models.Model):
    uniacid = models.PositiveIntegerField()
    acid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    filename = models.CharField(max_length=255)
    attachment = models.CharField(max_length=255)
    media_id = models.CharField(max_length=255)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    type = models.CharField(max_length=15)
    model = models.CharField(max_length=25)
    tag = models.CharField(max_length=5000)
    createtime = models.PositiveIntegerField()
    module_upload_dir = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ims_wechat_attachment'


class ImsWechatNews(models.Model):
    uniacid = models.PositiveIntegerField(blank=True, null=True)
    attach_id = models.PositiveIntegerField()
    thumb_media_id = models.CharField(max_length=60)
    thumb_url = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    digest = models.CharField(max_length=255)
    content = models.TextField()
    content_source_url = models.CharField(max_length=200)
    show_cover_pic = models.PositiveIntegerField()
    url = models.CharField(max_length=200)
    displayorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_wechat_news'


class ImsWeixinInfo(models.Model):
    content = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ims_weixin_info'


class ImsWxappGeneralAnalysis(models.Model):
    uniacid = models.IntegerField()
    session_cnt = models.IntegerField()
    visit_pv = models.IntegerField()
    visit_uv = models.IntegerField()
    visit_uv_new = models.IntegerField()
    type = models.IntegerField()
    stay_time_uv = models.CharField(max_length=10)
    stay_time_session = models.CharField(max_length=10)
    visit_depth = models.CharField(max_length=10)
    ref_date = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'ims_wxapp_general_analysis'


class ImsWxappVersions(models.Model):
    uniacid = models.PositiveIntegerField()
    multiid = models.PositiveIntegerField()
    version = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    modules = models.CharField(max_length=1000)
    design_method = models.IntegerField()
    template = models.IntegerField()
    quickmenu = models.CharField(max_length=2500)
    createtime = models.IntegerField()
    type = models.IntegerField()
    entry_id = models.IntegerField()
    appjson = models.TextField()
    default_appjson = models.TextField()
    use_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ims_wxapp_versions'


class ImsWxcardReply(models.Model):
    rid = models.PositiveIntegerField()
    title = models.CharField(max_length=30)
    card_id = models.CharField(max_length=50)
    cid = models.PositiveIntegerField()
    brand_name = models.CharField(max_length=30)
    logo_url = models.CharField(max_length=255)
    success = models.CharField(max_length=255)
    error = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ims_wxcard_reply'
