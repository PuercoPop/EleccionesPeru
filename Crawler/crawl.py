# -*- coding: utf-8 -*-

import urllib2
import psycopg2
import constants
import settings

from tasks import onpe_crawl

if __name__ == '__main__':
    """
    For type without parrent
    """

    conn = psycopg2.connect('dbname=%s user=%s' % (constants.dbname,
                                                   constants.user))
    cur = conn.cursor()
    cur.execute("""
        SELECT id, name, post_code, localidad
        FROM congreso_2011.post_codes 
        WHERE parent is NULL;
        """)
    rows = cur.fetchall()

    for row in rows:
        """
        Tentative breakdown
        compose_url
        fetch_data
        add_tasks
        """
        pk, name, post_code, place_type = row
        url = compose_url( localidad )
        r = fetch_data(url=url, post_code=post_code)
        #repartir tareas
        if place_type == 'region':
            r_name, r_post_code = onpe_crawl(url=, post_code)
            # Save in the return values with locidad: distritos and parent id
            cur.execute("""
                INSERT INTO congreso_2011.post_codes
                (name, post_code, localidad, parent) VALUES
                (%s, %s, 'provincia', %s)
                """ % ( r_name, r_post_code, pk))
            cur.commit()
