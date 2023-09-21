from prisma.models import Artist, Invoice, InvoiceItem, Customer, Employee, MediaType, Album, Playlist, PlaylistTrack, \
    Track, Genre

Album.create_partial(name="AlbumPostAndPut", include={"title", "artist_id"})
Artist.create_partial(name="ArtistPostAndPut", include={"name"})
Genre.create_partial(name="GenrePostAndPut", include={"name"})
Customer.create_partial(name="CustomerPostAndPut",
                        include={"first_name", "last_name", "company", "address", "city", "state", "country",
                                 "postal_code", "phone", "fax", "email", "support_rep_id"})
Employee.create_partial(name="EmployeePostAndPut",
                        include={"last_name", "first_name", "title", "birth_date", "hire_date", "address", "city",
                                 "state", "country", "postal_code", "phone", "fax", "email", "reports_to_id"})
Invoice.create_partial(name="InvoicePostAndPut",
                       include={"customer_id", "invoice_date", "billing_address", "billing_city", "billing_state",
                                "billing_country", "billing_postal_code", "total"})
InvoiceItem.create_partial(name="InvoiceItemPostAndPut", include={"invoice_id", "track_id", "unit_price", "quantity"})
MediaType.create_partial(name="MediaTypePostAndPut", include={"name"})
Playlist.create_partial(name="PlaylistPostAndPut", include={"name"})
PlaylistTrack.create_partial(name="PlaylistTrackPostAndPut", include={"playlist_id", "track_id"})
Track.create_partial(name="TrackPostAndPut",
                     include={"name", "album_id", "media_type_id", "genre_id", "composer", "milliseconds", "bytes",
                              "unit_price"})
