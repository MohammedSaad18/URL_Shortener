import { makeStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TablePagination from "@material-ui/core/TablePagination";
import TableRow from "@material-ui/core/TableRow";
import React, { useEffect, useState, useRef } from "react";
import axios from "axios";
import Link from "@material-ui/core/Link";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/typography";
import ClipboardJS from "clipboard";
const columns = [
  { id: "url", label: "URL", minWidth: 150 },
  // { id: "shortcode", label: "ShortCode", minWidth: 90 },
  // { id: "CreatedAt", label: "Created at", minWidth: 90 },
  // { id: "viewbutton", label: "", minWidth: 50 },
];

function createData(name, code, population, size) {
  const density = population / size;
  return { name, code, population, size, density };
}

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
  },
  container: {
    maxHeight: 440,
  },
  margin: {
    margin: theme.spacing(1),
  },
}));

export default function StickyHeadTable(props) {
  let [rows, setRows] = useState([]);
  const classes = useStyles();
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

  const shortURL = useRef(null);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/shorturls/")
      .then((response) => setRows(response.data));
  }, []);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  const copyShortURL = (id) => {
    const text = document.getElementById(id).href;
    let textArea = document.createElement("textarea");

    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
    // copyText.select();
    // document.execCommand("copy");
  };

  const represent_date = (date) => {
    date = new Date(date);
    return (
      date.getFullYear() +
      "-" +
      (date.getMonth() + 1) +
      "-" +
      date.getDate() +
      " " +
      date.getHours() +
      ":" +
      date.getMinutes()
    );
  };
  new ClipboardJS(".cpy");
  return (
    <React.Fragment>
      <TableContainer className={classes.container}>
        <Table stickyHeader aria-label="sticky table">
          {/* <TableHead>
            <TableRow>
              {columns.map((column) => (
                <TableCell
                  key={column.id}
                  align={column.align}
                  style={{ minWidth: column.minWidth }}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead> */}
          <TableBody>
            {rows
              .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              .map((row) => {
                return (
                  <TableRow
                    hover
                    role="checkbox"
                    tabIndex={-1}
                    key={row.shortcode}
                  >
                    <TableCell>
                      <div>
                        <time className="item-detail--created-date">
                          created {represent_date(row.created_at)}
                        </time>
                        <br />
                        <Typography variant="h4">{row.url_name}</Typography>
                        <br />
                        <Link target="_blank" color="secondary" href={row.url}>
                          {row.url}
                        </Link>
                        <br />
                        <Link
                          id={row.shortcode}
                          target="_blank"
                          color="primary"
                          href={`${row.shortcode}`}
                        >
                          clii.cc/{row.shortcode}
                        </Link>
                        <Button
                          variant="outlined"
                          size="small"
                          color="primary"
                          className={classes.margin}
                          onClick={() => copyShortURL(row.shortcode)}
                        >
                          Copy
                        </Button>

                        <Button
                          variant="outlined"
                          size="small"
                          color="primary"
                          className={classes.margin}
                          onClick={() => props.onURLView(row.shortcode)}
                        >
                          View Statistics
                        </Button>
                      </div>
                    </TableCell>
                    {/* <TableCell>{row.shortcode}</TableCell>
                    <TableCell>{represent_date(row.created_at)}</TableCell>
                    <TableCell>
                      <TimelineIcon
                        onClick={() => props.onURLView(row.shortcode)}
                        cursor="pointer"
                      />
                    </TableCell> */}
                  </TableRow>
                );
              })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[10, 25, 100]}
        component="div"
        count={rows.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onChangePage={handleChangePage}
        onChangeRowsPerPage={handleChangeRowsPerPage}
      />
    </React.Fragment>
  );
}
