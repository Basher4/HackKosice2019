using Xamarin.Forms;
using System;
using System.IO;

using Newtonsoft.Json.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace App5
{
    
    public partial class SchedulePage : ContentPage
    {
        public SchedulePage()
        {
            InitializeComponent();
        }

        
        HttpClient _client = new HttpClient();
        async void OnScheduleButtonClicked(object sender,EventArgs e)
        {
          
            TimeSpan opening_time= TimeSpan.Parse("8:00:00");
            TimeSpan interval = timePicker.Time - opening_time;
            if (id.Text == null)
            {
               await DisplayAlert("Error", "Prosim zadajte id pacienta", "OK");
                return;
            }

            JObject oJsonObject = new JObject();
            oJsonObject.Add("email", "None");
            oJsonObject.Add("id", id.Text);
            oJsonObject.Add("typ", "None");
            oJsonObject.Add("travel_time", 0);
            oJsonObject.Add("appointment_time", interval.Minutes);
            var stringContent = new StringContent(oJsonObject.ToString(), System.Text.Encoding.UTF8, "application/json");
            HttpResponseMessage response = await _client.PostAsync("https://hackkosice-2019-cakaren.appspot.com/api/patient/enqueue", stringContent);
            await Navigation.PopAsync();
        }
    }
}