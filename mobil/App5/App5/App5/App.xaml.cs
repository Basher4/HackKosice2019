using Xamarin.Forms;
using System;
using System.IO;
using Newtonsoft.Json.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Xamarin.Forms.Xaml;
[assembly: XamlCompilation(XamlCompilationOptions.Compile)]
namespace App5
{
    public partial class App : Application
    {


        public App()
        {
            InitializeComponent();


            MainPage = new LoadingPage();
        }


        protected override async void OnStart()
        {
            HttpResponseMessage response;
            HttpClient _client = new HttpClient();
            response = await _client.GetAsync("https://hackkosice-2019-cakaren.appspot.com/api/stats/status");
            if (response.IsSuccessStatusCode)
            {
                string str = await response.Content.ReadAsStringAsync();
                //string str = "";
                MainPage = new NavigationPage(new Uvodna(str)) { BarBackgroundColor = Color.FromHex("#545456"), BackgroundColor = Color.GhostWhite };

            }
            //else { MainPage = new MainPage(); }
        }


        protected override void OnSleep()
        {
            // Handle when your app sleeps
        }

        protected override void OnResume()
        {
            // Handle when your app resumes
        }
    }
}
