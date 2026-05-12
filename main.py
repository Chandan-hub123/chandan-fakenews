from predict import predict_news

print("📰 Fake News Detection System")
print("Type 'exit' to quit")

while True:
    news = input("\nEnter news: ")

    if news.lower() == "exit":
        print("Exiting system...")
        break

    result = predict_news(news)
    print("Result:", result)



