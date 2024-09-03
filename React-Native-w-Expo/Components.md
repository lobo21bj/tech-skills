# React Native / EXPO Components

<details>
    <summary>View</summary>
        Screen block similar to Div tag from HTML but including display flex by default.
</details>

<details>
    <summary>Text</summary>
        Text render component, usually it's inside the View.
</details>

<details>
    <summary>Image</summary>
        Used to render images.
        - Local: 
                ````md
                ```js
                import icon from './assets/icon.png'
                <Image source={icon} style ={{ width: 100, height: 100 }} />
                ```
                ````
        - External:
                ```js
                 <Image source={{ uri: "URL" }} style = {{ width: 215, height_ 294 }} />
                 ```
</details>