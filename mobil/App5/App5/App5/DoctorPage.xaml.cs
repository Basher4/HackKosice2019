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
            response = await _client.GetAsync("http://10.7.255.164:8080/api/stats/status");
            if (response.IsSuccessStatusCode)
            {
                string str = await response.Content.ReadAsStringAsync();
                Dictionary<string, string> info = JsonConvert.DeserializeObject<Dictionary<string, string>>(str);
                id.Text = info["id"];
            }
        }
        async void OnScheduleButtonClicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new SchedulePage());
        }
    }
}