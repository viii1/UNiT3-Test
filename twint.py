import twint

c = twint.Config()
c.Username = "username"
c.Custom["tweet"] = ["Sunaina17890221", "Sunaina Sharma"]
c.Output = "tweets.csv"
c.Store_csv = True

twint.run.Search(c)