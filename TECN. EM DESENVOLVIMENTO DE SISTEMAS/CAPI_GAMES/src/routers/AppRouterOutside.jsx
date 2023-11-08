import { BrowserRouter, Route, Routes } from 'react-router-dom';

import { Welcome, SignUp, Login, Error } from '../views/index'

import BaseLayout from "../layouts/BaseLayout";

const AppRouterOutside = () => {
    return (
        <BrowserRouter>
            <Routes >
                <Route>
                <Route path = "/" element = { <Welcome /> } />
                <Route path = "/Login" element = { <Login /> } />
                <Route path = "/Signup" element = { <SignUp /> } />
                <Route path = "*" element = { <Error />} />
                </Route>
            </Routes >
        </BrowserRouter>
    )                    
}

export default AppRouterOutside