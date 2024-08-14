namespace Moderation
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            string OPENAI_API_KEY = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
            Console.Write("Input Text: ");
            string text = Console.ReadLine();
            Console.WriteLine();
            var client = new HttpClient();
            var request = new HttpRequestMessage(HttpMethod.Post, "https://api.openai.com/v1/moderations");
            request.Headers.Add("Authorization", "Bearer " + OPENAI_API_KEY);
            var content = new StringContent($"{{\"input\": \"{text}\"}}", null, "application/json");
            request.Content = content;
            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();
            Console.WriteLine(await response.Content.ReadAsStringAsync());
        }
    }
}
