from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from dotenv import load_dotenv
import os
load_dotenv()
from supabase.client import Client, create_client

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)


class Berita(APIView):
    def get(self, request, *args, **kwargs):
        try:
            response = supabase.table('berita').select('*').execute()
            data = response.data
            return Response(response, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

# def historical_market_cap_detail(request, pk):
#     response = supabase.table('historical_market_cap').select('*').eq('id', pk).execute()
#     data = response.data
#     return Response(data)

