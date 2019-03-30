using Xamarin.Forms;
using System;
using System.IO;
using Org.Json;
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
        HttpResponseMessage response;
        string str;
        public App()
        {
            InitializeComponent();


            MainPage = new NavigationPage(new Uvodna(str));
        }

        protected override async void OnStart()
        {
            //HttpClient _client = new HttpClient();
            //response = await _client.GetAsync("https://8080-dot-6923620-dot-devshell.appspot.com/api/stats/status");
            //if (response.IsSuccessStatusCode)
            //{
            //    str = await response.Content.ReadAsStringAsync();

            //}
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
