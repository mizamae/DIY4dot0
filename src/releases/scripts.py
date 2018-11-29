import releases.models
import datetime
from django.conf import settings

def new_release():
    now = datetime.date.now()
    f = open(settings.RELEASES_TEMP, 'r')
    DjangoImage=File(f)
    RaspImage=File(f)
    
    REL=models.ReleaseModel.objects.create_Release(Date=now,Name='TestRelease',ChangeList='ChangeList',DjangoImage=DjangoImage,RaspImage=RaspImage)

def main():
    new_release()
    
if __name__ == '__main__':
    main()