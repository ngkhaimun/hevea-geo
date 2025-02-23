import folium
import streamlit as st

from service.unit import *
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Introduction",
    page_icon="👋", 
    layout="wide"
)


_dataset = [{"name":"Hevea KB","geometry":{"type":"Polygon","center_location":[4.747636,101.103208],"coordinates":[[4.748641,101.101674],[4.746631,101.101127],[4.746428,101.105515],[4.746909,101.105547],[4.74847,101.105268],[4.748641,101.101674]]}},{"name":"Hevea KB - Guard House","geometry":{"type":"Polygon","center_location":[4.747636,101.103208],"coordinates":[[4.748304,101.103026],[4.748277,101.103508],[4.748106,101.103508],[4.748144,101.103026],[4.748304,101.103026]]}},{"name":"SilverValley Technology Park","geometry":{"type":"Polygon","center_location":[4.746952,101.09948],"coordinates":[[4.746775,101.09911],[4.747165,101.09911],[4.747165,101.099877],[4.746775,101.099877],[4.746775,101.09911]]}},{"name":"Proposed Developments","geometry":{"type":"Polygon","center_location":[4.746299,101.097972],"coordinates":[[4.748769,101.099389],[4.745252,101.099313],[4.745273,101.096374],[4.748801,101.096395],[4.748769,101.099389]]}}]

# center on Liberty Bell, add marker
st.write(
        """
        Below is example of how inter-section detection, and trigger between : -
        - Hevea KB - Guard House & Hevea KB
        - Proposed Developments & SilverValley Technology Park
        """)



m = folium.Map(location=[4.747636, 101.1099], zoom_start=16 )


with st.sidebar:

    options = st.multiselect(
        "Choose geolocation for inter-section detection", 
        [d['name'] for d in _dataset],
        max_selections=2,
    )

    st.markdown("You have selected : " + str(options))
    
    _selected_locations = []
    if len(options) == 2:
        
        # get property of selected options
        for i, opt in enumerate(options):
            
            # add the selected location into LIST
            _selected_locations.append(get_location_data(opt, _dataset))

            folium.Polygon(
                get_location_data(opt, _dataset)['geometry']['coordinates'], 
                tooltip = get_location_data(opt, _dataset)['name'], 
            ).add_to(m)


        st.write("**Analysis for locations: -**")
        st.write("Distance (estimate) between points : {0} km(s)".format(str(
            calculate_distance(
                _selected_locations[0]['geometry']['center_location'], 
                _selected_locations[1]['geometry']['center_location']
            )))   
        )

        outer_poly = _selected_locations[0]['geometry']['coordinates']
        inner_poly = _selected_locations[1]['geometry']['coordinates']

        _outer_poly_name = _selected_locations[0]['name']
        _inner_poly_name = _selected_locations[1]['name']

        st.write("[**{0}**] is overlap by : {1}%".format(_outer_poly_name, overlap_percentage(inner_poly, outer_poly )))
        st.write("[**{0}**] is overlap by : {1}%".format(_inner_poly_name, overlap_percentage(outer_poly, inner_poly)))


st_folium(m, width=2000, height=700, returned_objects=[])

