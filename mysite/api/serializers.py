from rest_framework import serializers 
from .models import BlogPost 

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost 
        # 对应 BlogPost 模型 中的 title, content, published_date
        fields = ["id", "title", "content", "published_date"]