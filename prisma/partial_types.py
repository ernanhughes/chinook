from prisma.models import Artist, Invoice, InvoiceItem, Customer, Employee, MediaType, Album, Playlist, PlaylistTrack, Track, Genre

Album.create_partial(name="AlbumPostAndPut", include={"Title", "ArtistId"})
Artist.create_partial(name="ArtistPostAndPut", include={"Name"})
Genre.create_partial(name="GenrePostAndPut", include={"Name"})
Customer.create_partial(name="CustomerPostAndPut", include={"FirstName", "LastName", "Company", "Address", "City", "State", "Country", "PostalCode", "Phone", "Fax", "Email", "SupportRepId"})
Employee.create_partial(name="EmployeePostAndPut", include={"LastName", "FirstName", "Title", "BirthDate", "HireDate", "Address", "City", "State", "Country", "PostalCode", "Phone", "Fax", "Email"})
Invoice.create_partial(name="InvoicePostAndPut", include={"CustomerId", "InvoiceDate", "BillingAddress", "BillingCity", "BillingState", "BillingCountry", "BillingPostalCode", "Total"})
InvoiceItem.create_partial(name="InvoiceItemPostAndPut", include={"InvoiceId", "TrackId", "UnitPrice", "Quantity"})
MediaType.create_partial(name="MediaTypePostAndPut", include={"Name"})
Playlist.create_partial(name="PlaylistPostAndPut", include={"Name"})
PlaylistTrack.create_partial(name="PlaylistTrackPostAndPut", include={"PlaylistId", "TrackId"})
Track.create_partial(name="TrackPostAndPut", include={"Name", "AlbumId", "MediaTypeId", "GenreId", "Composer", "Milliseconds", "Bytes", "UnitPrice"})
