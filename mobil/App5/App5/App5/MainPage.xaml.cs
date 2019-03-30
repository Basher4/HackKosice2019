﻿
using Xamarin.Forms;
using System;
using System.IO;
using Org.Json;
using Newtonsoft.Json.Linq;
using System.Net.Http;
using System.Threading.Tasks;

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
         async Task OnSendButtonClicked(object sender, EventArgs e)
        {
            JObject oJsonObject = new JObject();
            oJsonObject.Add("e-mail", email.Text);
            oJsonObject.Add("id", id.Text);
            oJsonObject.Add("typ", data);
            string url = server.Text;
            var stringContent = new StringContent(oJsonObject.ToString(), System.Text.Encoding.UTF8, "application/json");
            HttpResponseMessage response = null;
            response =  await _client.PostAsync(url, stringContent);

            if (response.IsSuccessStatusCode)
            {
               server.Text="\tTodoItem successfully saved.";

            }

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