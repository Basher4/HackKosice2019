﻿
using Xamarin.Forms;
using System;
using System.IO;

using Newtonsoft.Json.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace App5
{
    public partial class MainPage : ContentPage
    {
        string data;
        public MainPage()
        {
            InitializeComponent();

           
        }
        HttpClient _client=new HttpClient();
         async void OnSendButtonClicked(object sender, EventArgs e)
        {
            JObject oJsonObject = new JObject();
            oJsonObject.Add("email", email.Text);
            oJsonObject.Add("id", id.Text);
            oJsonObject.Add("typ", data);
            oJsonObject.Add("travel_time", travel_time.Text);
            var stringContent = new StringContent(oJsonObject.ToString(), System.Text.Encoding.UTF8, "application/json");
            HttpResponseMessage response = null;
            response =  await _client.PostAsync("https://8080-dot-6923620-dot-devshell.appspot.com/api/patient/enqueue", stringContent);
            
           
           
        }
        void OnPickerSelectedIndexChanged(object sender, EventArgs e)
        {
            var picker = (Picker)sender;
            int selectedIndex = picker.SelectedIndex;

            if (selectedIndex != -1)
            {
              data = (string)picker.ItemsSource[selectedIndex];
            }
        }

    }
}
