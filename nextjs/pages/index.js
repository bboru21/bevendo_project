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
        const {
            deals,
            latest_pull_date: latestPullDate,
            cocktail_ingredients: cocktailIngredients,
        } = pageData;
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

                    {deals && (
                        <>
                            <h2>{`Weekly Virginia ABC Deals for ${latestPullDate}`}</h2>
                            <table>
                                <thead>
                                    <tr>
                                        <th>Product:</th>
                                        <th>Price (Below Avg/Size):</th>
                                        <th>On-Sale:</th>
                                        <th>Best Price:</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {deals.map( deal => (
                                        <tr>
                                            <td>
                                                <a href={`${deal.url}?productSize=${deal.product_size}`} target="_blank">
                                                    {deal.name} ({deal.size})
                                                </a>
                                            </td>
                                            <td>
                                                ${deal.current_price} (${deal.price_below_average_per_size})
                                            </td>
                                            <td>{ deal.is_on_sale ? 'YES': 'NO' }</td>
                                            <td>{ deal.is_best_price ? 'YES': 'NO' }</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </>
                    )}

                    {/*<h2>Most Common Cocktail Ingredients</h2>
                    <ol>
                        {cocktailIngredients.map( ingredient => (
                            <li>{`${ingredient.ingredient__name} (${ingredient.ingredient_count})`}</li>
                        ))}
                    </ol>*/}
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
