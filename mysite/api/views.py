from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.

# 博客文章列表和创建视图
class BlogPostListCreate(generics.ListCreateAPIView):
    # 指定查询集
    queryset = BlogPost.objects.all()
    # 指定序列化器
    serializer_class = BlogPostSerializer

    # 删除所有博客文章
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 博客文章详情、更新和删除视图
class BlogPostReteriveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    # 指定查询集
    queryset = BlogPost.objects.all()
    # 指定序列化器
    serializer_class = BlogPostSerializer
    # 指定主键字段
    lookup_field = "pk"

# 博客文章列表视图
class BlogPostList(APIView):
    def get(self, request, format=None):
        # 获取查询参数中的 title
        title = request.query_params.get('title', '')

        if title:
            # 根据 title 进行过滤
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            # 获取所有博客文章
            blog_posts = BlogPost.objects.all()

        # 序列化查询结果
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


