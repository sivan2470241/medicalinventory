from rest_framework import serializers
from .models import process_queue
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = process_queue
        fields =  ['process_id','title','process_file_location','process_status','return_status','return_json','call_back_url','call_back_status','call_back_json','process_entry_date']