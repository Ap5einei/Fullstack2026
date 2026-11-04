import {Link} from 'react-router';

const NavBar = () => {

    return(
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" style ={{marginLeft: 10}}>Contacts</a>
            < ul className = "navbar-nav">
                <li className="nav-item" style = {{marginLeft: 10}}>
                    <Link className="nav-link" to="/">Contact list</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/form">Add Contact</Link>
                </li>
            </ul>
        </nav>
    )
}

export default NavBar
