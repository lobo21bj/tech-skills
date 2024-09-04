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

- Internal: 
```js
import icon from './assets/icon.png'
<Image source={icon} style ={{ width: 100, height: 100 }} />
```
- External:
```js
<Image source={{ uri: "URL" }} style = {{ width: 215, height_ 294 }} />
```
</details>

<details>
    <summary>StatusBar</summary>
        Expo component that changes the mobile status bar color.

```js
import { StatusBar } from 'expo-status-bar';
```
</details>

<details>
    <summary>Button</summary>
        React Native button component for each OS, cannot be styled.
        
```js
import Button from 'react-native'

<Button title="Click here" onPress={() => alert('Warning')} />
```
</details>

<details>
    <summary>TouchableHighlight or TouchableOpacity</summary>
        React Native button component as well with feedback animation when the user clicks on it.
        
```js
import TouchableHighlight from 'react-native'

<TouchableHighlight
    underlayColor={'red'}
    onPress={() => alert('hola')}
    Style={{ xxxx}}
>
    <Text style={{ color: 'white' }}>Pulsa Aquí</Text>
</TouchableHighlight>
```
</details>

<details>
    <summary>Pressable</summary>
        Core button component of React Native. It's the most commonly used. Includes different kinds of press: in, out, long.
        
```js
import Pressable from 'react-native'

<Pressable onPress={onPressFunction}>
<Text>I'm pressable!</Text>
</Pressable>
```
</details>

<details>
    <summary>ScrollView</summary>
        React Native component to scroll content. Due to render all at once, it's useful for text screens.
        
```js
import ScrollView from 'react-native'

<ScrollView>
    {games.map((game) => (
        <GameCard key={game.slug} gane={game} />
    ))}
</ScrollView>
```
</details>

<details>
    <summary>FlatList</summary>
        React Native component to scroll with high performance. It renders while it goes thru the list.
        
```js
import FlatList from 'react-native'

<FlatList
    data={games}
    keyExtractor={(game) => game.slug}
    renderItem={({ item }) => <GameCard game={item} />}
/>
```
</details>

<details>
    <summary>SafeAreaView</summary>
        React Native component that works as a view with padding to avoid overlapping with the status bar.
        
```js
import SafeAreaView from 'react-native-safe-area-context'

<SafeAreaView style={styles.container}>
    <Text style={styles.text}>Page content</Text>
</SafeAreaView>
```
</details>

<details>
    <summary>ActivityIndicator</summary>
        React Native component to add an animation while the app gets render.

```js
import ActivityIndicator from 'react-native'

<View style={[styles.container, styles.horizontal]}>
    <ActivityIndicator />
    <ActivityIndicator size="large" />
</View>
```
</details>

<details>
    <summary>SplashScreen</summary>
        Expo component to keep the screen with any custom content while the app process any backend operation, sample usage: logo picture when the app starts.
        
```js
import SplashScreen from 'expo-splash-screen'
```
</details>