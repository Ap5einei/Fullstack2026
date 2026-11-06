import{Link} from 'react-router';

const NavBar =() => {
    return(
        <nav className='navbar navbar-expand-lg navbar-light bg-light'>
            <a className="navbar-brand" style={{marginLeft:10}}>Shopping 
                App
            </a>
            <ul className = "navbar-nav">
                <li className="nav-item" style ={{marginLeft:10}}>
                    <Link to = "/" className = "nav-link"> Shopping List </Link>
                </li>
                <li className="nav-item" style ={{marginLeft:10}}>
                    <Link to = "/" className = "nav-link"> ADD new item </Link>
                </li>
            </ul>
        </nav>

    )
}

export default NavBar;