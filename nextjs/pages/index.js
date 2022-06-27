import React from 'react';
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pageData: {},
        };
    }

    componentDidMount() {
        const data = JSON.parse(document.getElementById('pageData').textContent);
        this.setState({...this.state, pageData: data });
    }

    render() {
        const { pageData } = this.state;
        const { foo } = pageData;
        return (
            <div className={styles.container}>
                <Head>
                    <title>Bevendo: A Companion App to Drinking with the Saints</title>
                    <link rel="icon" href="/favicon.ico" />
                </Head>

                  <main className={styles.main}>
                    <h1 className={styles.title}>
                        Bevendo!
                    </h1>

                    <p className={styles.description}>
                        A companion app to "Drinking with the Saints".
                    </p>

                    <pre>{foo && foo}</pre>

                </main>

                <footer className={styles.footer}>
                    <a
                        href="http://bryanhadro.com"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Powered by{' '}
                        <span className={styles.logo}>
                            BryanHadro.com
                        </span>
                    </a>
                </footer>
            </div>
        );
    }
}

export default Home;
