# login
Link to [Challenge] (https://play.picoctf.org/practice/challenge/200)

### Description
My dog-sitter's brother made this website but I can't get in; can you help?
(login.mars.picoctf.net) [login.mars.picoctf.net]

### Challenge
When we first navigate to the website we see a rather plain looking login page.

![login page](/login/imgs/login_page.png)

My first thought when probing a login page like this is to try the credentials user: `admin` pass: `admin`. After trying this we see this alert pop up.

![Incorrect login alert](/login/imgs/incorrect_login_alert.png)

This is a javascript alert, after seeing I think that login validation may be done on the client side and begin to look at the HTML and Js sources for this page.


```
index.html

<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="styles.css">
        <script src="index.js"></script>
    </head>
    <body>
        <div>
          <h1>Login</h1>
          <form method="POST">
            <label for="username">Username</label>
            <input name="username" type="text"/>
            <label for="username">Password</label>
            <input name="password" type="password"/>
            <input type="submit" value="Submit"/>
          </form>
        </div>
    </body>
</html>
```

In this HTML we can see there is a Js static file that is also pulled.

```
index.js

(async()=>{
    await new Promise((e=>window.addEventListener("load", e))),
    document.querySelector("form").addEventListener("submit", (e=>{
        e.preventDefault();
        const r = {
            u: "input[name=username]",
            p: "input[name=password]"
        }
          , t = {};
        for (const e in r)
            t[e] = btoa(document.querySelector(r[e]).value).replace(/=/g, "");
        return "YWRtaW4" !== t.u ? alert("Incorrect Username") : "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ" !== t.p ? alert("Incorrect Password") : void alert(`Correct Password! Your flag is ${atob(t.p)}.`)
    }
    ))
}
)();
```
