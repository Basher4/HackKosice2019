using Xamarin.Forms;
using System;
using System.IO;

using Newtonsoft.Json.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using System.Collections.Generic;

namespace App5
{

    public partial class DoctorPage : ContentPage
    {
        public DoctorPage()
        {
            InitializeComponent();
        }

        HttpResponseMessage response;
        HttpClient _client = new HttpClient();
        async void OnSendButtonClicked(object sender, EventArgs e)
        {
            response = await _client.GetAsync("https://hackkosice-2019-cakaren.appspot.com/api/doctor/entered");
            if (response.IsSuccessStatusCode)
            {
                string str = await response.Content.ReadAsStringAsync();
                if (str.Length >=4) { 
                    Dictionary<string, string> info = JsonConvert.DeserializeObject<Dictionary<string, string>>(str);
                    id.Text = info["id"];
                }
                else { id.Text = "Žiadny ďalší pacient v poradí"; };
            }
        }
        async void OnScheduleButtonClicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new SchedulePage());
        }
    }
}