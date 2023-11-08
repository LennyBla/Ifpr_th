import "./styles/main.scss";
import { Provider } from 'react-redux';
import AppRouter from "./routers/AppRouter";
import store from "./redux/store/store";
import AppRouterOutside from "./routers/AppRouterOutside";

function App() {

  const user = false

  if(user){

    return (
      <div className="App">
        <Provider store={ store }>
          <AppRouter />
        </Provider>
      </div>
    )
  } else {
    console.log('ops');
      return (
    
         <AppRouterOutside/>
      )
  }
}

export default App
