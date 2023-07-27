import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { GroceryLists } from './pages/GroceryLists';

function App() {
  return (
    <Router>
        <Routes>
            <Route exact path='/' exact element={<Home />} />
            <Route path='/login' element={<Login />} />
            <Route path='/register' element={<Register />} />
            <Route path='/blogs' element={<GroceryLists />} />
            <Route path='/sign-up' element={<SignUp />} />
        </Routes>
    </Router>
  );
}

export default App;
