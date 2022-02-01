/*
*    Proof of concept for building an HTML Reporting API
*    in Oracle DB 12c with a PL/SQL Package
*/

CREATE OR REPLACE PACKAGE html AS 
    -- A list type to allow deep nesting of elements
    TYPE list IS TABLE OF varchar2(32000);
    
    -- Functions that build out html elements
    FUNCTION page       (p_list list) RETURN CLOB;
    FUNCTION head       (p_list list) RETURN CLOB;
    FUNCTION body       (p_list list) RETURN CLOB;
    FUNCTION h1         (p_list list, p_style varchar2 default null) RETURN CLOB;
    FUNCTION p          (p_list list, p_style varchar2 default null) RETURN CLOB;
    FUNCTION htable     (p_list list) RETURN CLOB;
    FUNCTION th         (p_list list) RETURN CLOB;
    FUNCTION tr         (p_list list) RETURN CLOB;
    FUNCTION td         (p_list list) RETURN CLOB;
    FUNCTION style      (p_list list) RETURN CLOB;
    
    -- Write the report out to a diectory
    PROCEDURE write_report    (p_report CLOB, p_fileName varchar2, p_dir varchar2);
END;
/
create or replace package body html as
    

    -- The workhorse that fills nested tags
    FUNCTION fillTag (p_list list, p_opentag clob, p_closetag clob)
    RETURN CLOB IS
        l_results   CLOB := p_opentag;
    BEGIN
        
        FOR e in p_list.first..p_list.last LOOP
            l_results := l_results||chr(10)||p_list(e)||chr(10);
        END LOOP;
        
        l_results := l_results||p_closetag;
        RETURN l_results;
    END fillTag;    
    
    /* Start the tag wrapper functions */
    FUNCTION style (p_list list) RETURN CLOB
    IS
        c_opentag   clob    := '<style>';
        c_closetag  clob    := '</style>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);
    END style;
    
    FUNCTION page (p_list list) RETURN CLOB
    IS
        c_opentag   clob    := '<!DOCTYPE html>'||chr(10)||'<html lang="en">'||chr(10);
        c_closetag  clob    := chr(10)||'</html>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);
    END;
    
    FUNCTION head (p_list list) RETURN CLOB
    IS
        c_opentag   clob    := '<head>';
        c_closetag  clob    := '</head>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);
    END head;
    
    FUNCTION body (p_list list) RETURN CLOB
    IS
        c_opentag   clob    := '<body>';
        c_closetag  clob    := '</body>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);        
    END body;
    
    FUNCTION h1 (p_list list, p_style varchar2 DEFAULT null) RETURN CLOB
    IS
        c_opentag   clob    := '<h1 style="'||p_style||'">';
        c_closetag  clob    := '</h1>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);
    end h1;
    
    FUNCTION p (p_list list, p_style varchar2 DEFAULT null) RETURN CLOB
    IS
        c_opentag   clob    := '<p style="'||p_style||'">';
        c_closetag  clob    := '</p>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);        
    END p;
    
    FUNCTION htable (p_list list) RETURN CLOB
    IS
        c_opentag   clob    := '<table>';
        c_closetag  clob    := '</table>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);
    END htable;
    
    FUNCTION th (p_list list) RETURN CLOB
    IS
        c_opentag   clob    := '<th>';
        c_closetag  clob    := '</th>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);
    END th;
    
    FUNCTION tr (p_list list) RETURN CLOB
    IS
        c_opentag   clob    := '<tr>';
        c_closetag  clob    := '</tr>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);
    END tr;
    
    FUNCTION td (p_list list) RETURN CLOB
    IS
        c_opentag   clob    := '<td>';
        c_closetag  clob    := '</td>';
    BEGIN
        RETURN html.fillTag(p_list, c_opentag, c_closetag);
    END td;
    

    -- Used to write out reports
    PROCEDURE write_report (p_report CLOB, p_fileName varchar2, p_dir varchar2)
    IS
        fhandle UTL_FILE.FILE_TYPE;
    BEGIN
        -- Create or overwrite the file
        fhandle := UTL_FILE.FOPEN(p_dir, p_fileName, 'w');
        
        UTL_FILE.PUT(fhandle, p_report);
        
        UTL_FILE.FCLOSE(fhandle);
    END write_report;
    
END html;
