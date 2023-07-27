import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { GroceryLists } from './pages/GroceryLists';
import { GroceryList } from './pages/GroceryList';
import { Home } from './pages/Home';

function App() {
  return (
    <Router>
        <Routes>
            <Route exact path='/' element={<Home />} />
            <Route path='/login' element={<Login />} />
            <Route path='/register' element={<Register />} />
            <Route path='/g_lists' element={<GroceryLists />} />
            <Route path='/g_list' element={<GroceryList />} />
        </Routes>
    </Router>
  );
}

export default App;
