from django.db import models

class Albums(models.Model):
    album_id = models.CharField(primary_key=True, max_length=50)
    album_name = models.CharField(max_length=150, blank=True, null=True)
    album_artist = models.CharField(max_length=50, blank=True, null=True)
    album_genre = models.CharField(max_length=50, blank=True, null=True)
    album_image = models.CharField(max_length=150, blank=True, null=True)
    album_release_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'albums'


class Alternative(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alternative'


class AudioFeatures(models.Model):
    track = models.OneToOneField('Tracks', models.DO_NOTHING, primary_key=True)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audio_features'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersAppUser', models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Electro(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'electro'


class Hiphop(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hiphop'


class Indiepop(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indiepop'


class Jazz(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jazz'


class Jpop(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jpop'


class Kpop(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kpop'


class KwdSearch(models.Model):
    search_no = models.BigAutoField(primary_key=True)  # The composite primary key (search_no, id) found, that is not supported. The first column is selected.
    id = models.ForeignKey('UsersAppUser', models.DO_NOTHING, db_column='id')
    album_kw = models.CharField(max_length=100, blank=True, null=True)
    track_kw = models.CharField(max_length=100, blank=True, null=True)
    genre_kw = models.CharField(max_length=100, blank=True, null=True)
    artist_kw = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kwd_search'
        unique_together = (('search_no', 'id'),)


class Latin(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'latin'


class LikedAlbum(models.Model):
    la_no = models.AutoField(db_column='LA_no', primary_key=True)  # Field name made lowercase.
    id = models.ForeignKey('UsersAppUser', models.DO_NOTHING, db_column='id')
    album = models.ForeignKey(Albums, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'liked_album'

class LikedTrack(models.Model):
    lt_no = models.IntegerField(db_column='LT_no', primary_key=True)  # Field name made lowercase.
    track = models.ForeignKey('Tracks', models.DO_NOTHING)
    id = models.ForeignKey('UsersAppUser', models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liked_track'

class PlayList(models.Model):
    playlist_no = models.AutoField(primary_key=True)
    id = models.ForeignKey('UsersAppUser', models.DO_NOTHING, db_column='id')
    track = models.ForeignKey('Tracks', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'play_list'


class Rnb(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rnb'


class Rock(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    acousticness = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rock'


class Tracks(models.Model):
    track_id = models.CharField(primary_key=True, max_length=50)
    track_name = models.CharField(max_length=150, blank=True, null=True)
    track_preview = models.CharField(max_length=150, blank=True, null=True)
    album = models.ForeignKey(Albums, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tracks'


class UsersAppUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    user_name = models.CharField(max_length=100)
    user_genre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'users_app_user'


class UsersAppUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersAppUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_app_user_groups'
        unique_together = (('user', 'group'),)


class UsersAppUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersAppUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_app_user_user_permissions'
        unique_together = (('user', 'permission'),)