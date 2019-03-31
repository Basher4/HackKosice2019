
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
        string data="";
        public MainPage()
        {
            InitializeComponent();

           
        }
        HttpClient _client=new HttpClient();
         async void OnSendButtonClicked(object sender, EventArgs e)
        {
            if (id.Text.Length == 0 || (data.Length == 0) || email.Text.Length==0  || travel_time.Text.Length == 0)
            {
                await DisplayAlert("Error", "Prosim zadajte vsetky udaje", "OK");
                return;
            }

            JObject oJsonObject = new JObject();
            oJsonObject.Add("email", email.Text);
            oJsonObject.Add("id", id.Text);
            oJsonObject.Add("typ", data);
            oJsonObject.Add("travel_time", travel_time.Text);
            oJsonObject.Add("appointment_time", "None");
            var stringContent = new StringContent(oJsonObject.ToString(), System.Text.Encoding.UTF8, "application/json");
            HttpResponseMessage response = null;
            response =  await _client.PostAsync("http://10.7.255.164:8080/api/patient/enqueue", stringContent);
            
           
           
        }
        void SelectedIndexChanged(object sender, EventArgs e)
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
