from rest_framework import serializers
from .models import Book2, Author ,Books
from django.db.models import Q
from .utils.exceptions import customBadRequest
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class Serial(serializers.ModelSerializer):
    # def validate(self, data):
    #     # if data["title"]:
    #     #     print("abc")
    #     if data['title'] == data['genre']:
    #         raise serializers.ValidationError("Title and Genre cannot be same")
    #     return data
    class Meta:
        model = Book2
        fields = '__all__'
        # extra_kwargs = {
        #     # 'author':{'required':False},
        #     # 'publisher':{'required':False},
        #     'title':{'required':False},
        #     'genre':{'required':False},
        #     # 'published_date':{'required':False},
        # }
        
    def validate(self, data):
        
        titlec=data.get('title')
        genrec=data.get('genre')
        # genred = Book2.objects.get(Q(genre=titlec) | Q(title=genrec))
        # titled = Book2.objects.get(title=genrec)
        if titlec == genrec or Book2.objects.filter(Q(genre=titlec) | Q(title=genrec)):
            raise serializers.ValidationError("Title and Genre cannot be same")
        return data 
    
    def validate_price(self,value):
        if value < 400:
            raise customBadRequest("Price must be greater than 400")
        return value
    
    
    
        
        
class Serial2(serializers.ModelSerializer):
    # content = serializers.JSONField()
    # title = serializers.CharField(max_length=100, required=False)
    # genre = serializers.CharField(max_length=200, required=False)
    # price = serializers.IntegerField()
    # published_date = serializers.DateField(required=False)
    # author = serializers.(required=False)
    # publisher = serializers.(required=False)
    # created_at = serializers.DateTimeField()
    # updated_on = serializers.()
    
    class Meta:
        model = Book2
        # fields = ('content',)
        fields = "__all__"
        # extra_kwargs = {
            # 'author':{'required':False},
            # 'publisher':{'required':False},
            # 'title':{'required':False},
            # 'genre':{'required':False},
            # 'published_date':{'required':False},
        # }
    def validate(self, data):
        if data['title'] == data["genre"]:
            raise serializers.ValidationError("Title and Genre cannot be same")
        return data
    # def create(self, validated_data):
    #     return Book2.create(validated_data)
    
class Author_Serial(serializers.ModelSerializer):
    # books2 = serializers.StringRelatedField(many=True, read_only=True)
    # books2 = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # website_book2_related = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='author_view')
    # website_book2_related = serializers.HyperlinkedIdentityField(view_name='author_view')
    # website_book2_related = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    
    class Meta:
        model=Author
        fields = "__all__"
        
    # def validate(self, data):
    #     # if data["title"]:
    #     #     print("abc")
    #     fnamec=data.get('firstname')
    #     lnamec=data.get('lastname')
    #     # genred = Book2.objects.get(Q(genre=titlec) | Q(title=genrec))
    #     # titled = Book2.objects.get(title=genrec)
    #     if fnamec == lnamec or Author.objects.filter(Q(lastname=fnamec) | Q(firstname=lnamec)):
    #         raise serializers.ValidationError("Firstname and Lastname cannot be same")
    #     return data 
    #     # if data['firstname'] == data['lastname']:
    #     #     raise serializers.ValidationError("Title and Genre cannot be same")
    #     # return data 