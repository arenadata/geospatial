Summary:        Geospatial extensions for Greenplum Database
License:        GPLv2
Name:           postgis
Version:        %{postgis_ver}
Release:        %{postgis_rel}
Group:          Development/Tools
Prefix:         /usr
AutoReq:        no
AutoProv:       no
Provides:       postgis = %{postgis_ver}
Requires:       geos = %{geos_ver}, proj = %{proj_ver}, json-c = %{json_ver}, gdal = %{gdal_ver}

%description
The PostGIS module provides geospatial extensions for Greenplum Database.

%install
make -C %{postgis_dir} BLD_TOP=%{bld_top} install prefix=%{buildroot}%{_prefix}

mkdir -p %{buildroot}%{_prefix}/bin
cp $GPHOME/bin/pgsql2shp %{buildroot}%{_prefix}/bin
cp $GPHOME/bin/shp2pgsql %{buildroot}%{_prefix}/bin
cp $GPHOME/bin/raster2pgsql %{buildroot}%{_prefix}/bin

mkdir -p %{buildroot}%{_prefix}/lib/postgresql
cp $GPHOME/lib/postgresql/postgis-2.1.so %{buildroot}%{_prefix}/lib/postgresql/postgis-2.1.so
cp $GPHOME/lib/postgresql/rtpostgis-2.1.so %{buildroot}%{_prefix}/lib/postgresql/rtpostgis-2.1.so

mkdir -p %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/
mkdir -p %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/{install,upgrade,uninstall}/

cp $GPHOME/share/postgresql/contrib/postgis-2.1/postgis.sql %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/rtpostgis.sql %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/*comments.sql %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/spatial_ref_sys.sql %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/install/

cp $GPHOME/share/postgresql/contrib/postgis-2.1/*upgrade*.sql %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/legacy*.sql %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/rtpostgis_legacy.sql %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/

cp $GPHOME/share/postgresql/contrib/postgis-2.1/uninstall*.sql %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/uninstall/

cp %{postgis_dir}/../../package/postgis_manager.sh %{buildroot}%{_prefix}/share/postgresql/contrib/postgis-2.1/postgis_manager.sh

%files
%{_prefix}/bin/pgsql2shp
%{_prefix}/bin/raster2pgsql
%{_prefix}/bin/shp2pgsql
%{_prefix}/include/liblwgeom.h
%{_prefix}/lib/liblwgeom-2.1.5.so
%{_prefix}/lib/liblwgeom.a
%{_prefix}/lib/liblwgeom.la
%{_prefix}/lib/liblwgeom.so
%{_prefix}/lib/postgresql/postgis-2.1.so
%{_prefix}/lib/postgresql/rtpostgis-2.1.so
%{_prefix}/share/postgresql/contrib/postgis-2.1/postgis_manager.sh
%{_prefix}/share/postgresql/contrib/postgis-2.1/install/postgis.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/install/postgis_comments.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/install/raster_comments.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/install/rtpostgis.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/install/spatial_ref_sys.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/install/topology_comments.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/topology_upgrade_21_minor.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_legacy.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_postgis.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_rtpostgis.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_sfcgal.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_topology.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/legacy.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/legacy_gist.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/legacy_minimal.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/postgis_upgrade_20_21.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/postgis_upgrade_21_minor.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/rtpostgis_legacy.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/rtpostgis_upgrade_20_21.sql
%{_prefix}/share/postgresql/contrib/postgis-2.1/upgrade/rtpostgis_upgrade_21_minor.sql
